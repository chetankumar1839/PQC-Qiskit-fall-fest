import json
import uuid
from pathlib import Path
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field
from sqlalchemy import select
from sqlalchemy.orm import Session

from .database import engine, get_db
from .models import Base, Official, LandRecord, Transaction, Alert, AuditEvent
from .ai_monitor import ActivityMonitor
from .quantum_risk import quantum_risk_qiskit
from .pqc_wrapper import PQCWrapper
from .ledger import append_audit, verify_chain

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Quantum-Safe Land Record Security")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

monitor = ActivityMonitor()
pqc = PQCWrapper()

class TransactionRequest(BaseModel):
    survey_no: str
    official_id: str
    new_area: float = Field(gt=0)
    document_consistent: bool = True
    jurisdiction_match: bool = True
    login_security_anomaly: bool = False
    repeated_modifications: int = Field(default=0, ge=0)

@app.on_event("startup")
def seed():
    from .database import SessionLocal
    db = SessionLocal()
    try:
        if not db.execute(select(Official)).scalars().first():
            db.add_all([
                Official(
                    official_id="OFF-1001",
                    name="Ravi Kumar",
                    designation="Revenue Officer",
                    jurisdiction="Vizianagaram",
                ),
                Official(
                    official_id="OFF-1047",
                    name="Demo Official",
                    designation="Revenue Officer",
                    jurisdiction="Vizianagaram",
                ),
            ])

        if not db.execute(select(LandRecord)).scalars().first():
            db.add_all([
                LandRecord(
                    survey_no="145/2",
                    owner_name="Ramesh Kumar",
                    village="Demo Village",
                    area_acres=3.25,
                ),
                LandRecord(
                    survey_no="210/4",
                    owner_name="Sita Devi",
                    village="Demo Village",
                    area_acres=2.00,
                ),
            ])
        db.commit()
    finally:
        db.close()

@app.get("/")
def root():
    return FileResponse(
        Path(__file__).resolve().parent.parent / "frontend" / "index.html"
    )

@app.get("/api/health")
def health(db: Session = Depends(get_db)):
    return {"status": "ok", "audit_chain_valid": verify_chain(db)}

@app.get("/api/officials")
def officials(db: Session = Depends(get_db)):
    rows = db.execute(select(Official).where(Official.active == True)).scalars().all()
    return [
        {
            "official_id": x.official_id,
            "name": x.name,
            "designation": x.designation,
            "jurisdiction": x.jurisdiction,
        } for x in rows
    ]

@app.get("/api/land-records")
def land_records(db: Session = Depends(get_db)):
    rows = db.execute(select(LandRecord).order_by(LandRecord.id)).scalars().all()
    return [
        {
            "survey_no": x.survey_no,
            "owner_name": x.owner_name,
            "village": x.village,
            "area_acres": x.area_acres,
            "version": x.version,
        } for x in rows
    ]

@app.post("/api/transactions")
def create_transaction(req: TransactionRequest, db: Session = Depends(get_db)):
    record = db.execute(
        select(LandRecord).where(LandRecord.survey_no == req.survey_no)
    ).scalars().first()
    if not record:
        raise HTTPException(404, "Land record not found")

    official = db.execute(
        select(Official).where(Official.official_id == req.official_id)
    ).scalars().first()
    if not official:
        raise HTTPException(404, "Official not found")

    classical_risk, reasons = monitor.score(
        record.area_acres,
        req.new_area,
        req.document_consistent,
        req.jurisdiction_match,
        req.login_security_anomaly,
        req.repeated_modifications,
    )

    change_ratio = abs(req.new_area - record.area_acres) / max(record.area_acres, 0.01)
    quantum_features = [
        min(change_ratio, 1.0),
        0 if req.document_consistent else 1,
        min(
            (
                (0 if req.jurisdiction_match else 1)
                + (1 if req.login_security_anomaly else 0)
                + min(req.repeated_modifications / 5, 1)
            ) / 3,
            1.0,
        ),
    ]

    q = quantum_risk_qiskit(quantum_features)
    quantum_risk = q["risk"]

    combined = round((0.70 * classical_risk) + (0.30 * quantum_risk), 4)
    pqc_result = pqc.verify_and_respond(combined)

    if combined <= 0.30:
        decision = "ALLOW"
        status = "MONITORING"
    elif combined <= 0.50:
        decision = "ROTATE_KEYS"
        status = "PQC_REESTABLISHED"
    else:
        decision = "BLOCK"
        status = "QUARANTINED"

    tx_id = "TX-" + uuid.uuid4().hex[:10].upper()

    tx = Transaction(
        tx_id=tx_id,
        survey_no=record.survey_no,
        official_id=official.official_id,
        old_area=record.area_acres,
        new_area=req.new_area,
        document_consistent=req.document_consistent,
        jurisdiction_match=req.jurisdiction_match,
        login_security_anomaly=req.login_security_anomaly,
        repeated_modifications=req.repeated_modifications,
        classical_risk=classical_risk,
        quantum_risk=quantum_risk,
        combined_risk=combined,
        pqc_status=pqc_result["status"],
        decision=decision,
        status=status,
    )
    db.add(tx)

    append_audit(
        db, tx_id, "TRANSACTION_ANALYZED",
        json.dumps({
            "official_id": official.official_id,
            "survey_no": record.survey_no,
            "classical_risk": classical_risk,
            "quantum_risk": quantum_risk,
            "combined_risk": combined,
            "decision": decision,
            "reasons": reasons,
        }),
    )

    # Only suspicious transactions create alerts.
    if combined > 0.50:
        owner_msg = (
            f"Suspicious activity on Survey No. {record.survey_no}. "
            f"Change {record.area_acres} -> {req.new_area} acres. "
            f"Risk {combined:.0%}. Transaction quarantined."
        )
        supervisor_msg = (
            f"High-risk transaction {tx_id} by {official.official_id}. "
            f"Survey {record.survey_no}; risk {combined:.0%}. "
            f"Human verification required."
        )
        db.add(Alert(
            tx_id=tx_id, recipient_type="LAND_OWNER",
            recipient=record.owner_name, message=owner_msg
        ))
        db.add(Alert(
            tx_id=tx_id, recipient_type="SUPERVISOR",
            recipient=official.jurisdiction, message=supervisor_msg
        ))
        append_audit(
            db, tx_id, "ALERTS_SENT",
            "Land owner and supervisory officials notified."
        )

    # Only an allowed transaction changes the authoritative record.
    if decision == "ALLOW":
        record.area_acres = req.new_area
        record.version += 1
        append_audit(
            db, tx_id, "RECORD_UPDATED",
            f"Survey {record.survey_no} updated to {req.new_area} acres."
        )

    db.commit()

    return {
        "tx_id": tx_id,
        "survey_no": record.survey_no,
        "official": official.official_id,
        "owner": record.owner_name,
        "classical_risk": classical_risk,
        "quantum_risk": quantum_risk,
        "combined_risk": combined,
        "risk_percent": round(combined * 100, 1),
        "reasons": reasons,
        "pqc": pqc_result,
        "decision": decision,
        "status": status,
        "quantum_backend": q["backend"],
        "quantum_counts": q["counts"],
        "quantum_circuit": q["circuit"],
    }

@app.get("/api/transactions")
def transactions(db: Session = Depends(get_db)):
    rows = db.execute(
        select(Transaction).order_by(Transaction.id.desc())
    ).scalars().all()
    return [
        {
            "tx_id": x.tx_id,
            "survey_no": x.survey_no,
            "official_id": x.official_id,
            "classical_risk": x.classical_risk,
            "quantum_risk": x.quantum_risk,
            "combined_risk": x.combined_risk,
            "decision": x.decision,
            "status": x.status,
            "created_at": x.created_at.isoformat(),
        } for x in rows
    ]

@app.get("/api/alerts")
def alerts(db: Session = Depends(get_db)):
    rows = db.execute(
        select(Alert).order_by(Alert.id.desc())
    ).scalars().all()
    return [
        {
            "tx_id": x.tx_id,
            "recipient_type": x.recipient_type,
            "recipient": x.recipient,
            "message": x.message,
            "sent": x.sent,
            "created_at": x.created_at.isoformat(),
        } for x in rows
    ]

@app.get("/api/audit")
def audit(db: Session = Depends(get_db)):
    rows = db.execute(
        select(AuditEvent).order_by(AuditEvent.id.desc())
    ).scalars().all()
    return [
        {
            "id": x.id,
            "tx_id": x.tx_id,
            "event_type": x.event_type,
            "details": x.details,
            "event_hash": x.event_hash,
            "previous_hash": x.previous_hash,
            "created_at": x.created_at.isoformat(),
        } for x in rows
    ]
