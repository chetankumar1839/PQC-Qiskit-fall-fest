import hashlib
import json
from datetime import datetime
from sqlalchemy import select

from .models import AuditEvent

def append_audit(db, tx_id, event_type, details):
    last = db.execute(
        select(AuditEvent).order_by(AuditEvent.id.desc())
    ).scalars().first()

    previous_hash = last.event_hash if last else ""
    payload = {
        "tx_id": tx_id,
        "event_type": event_type,
        "details": details,
        "previous_hash": previous_hash,
        "created_at": datetime.utcnow().isoformat(),
    }
    event_hash = hashlib.sha256(
        json.dumps(payload, sort_keys=True).encode()
    ).hexdigest()

    event = AuditEvent(
        tx_id=tx_id,
        event_type=event_type,
        details=details,
        previous_hash=previous_hash,
        event_hash=event_hash,
    )
    db.add(event)
    db.commit()
    return event

def verify_chain(db):
    events = db.execute(
        select(AuditEvent).order_by(AuditEvent.id.asc())
    ).scalars().all()

    previous = ""
    for e in events:
        if e.previous_hash != previous:
            return False
        payload = {
            "tx_id": e.tx_id,
            "event_type": e.event_type,
            "details": e.details,
            "previous_hash": e.previous_hash,
            "created_at": e.created_at.isoformat(),
        }
        expected = hashlib.sha256(
            json.dumps(payload, sort_keys=True).encode()
        ).hexdigest()
        if expected != e.event_hash:
            return False
        previous = e.event_hash
    return True
