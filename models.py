from datetime import datetime
from sqlalchemy import Boolean, DateTime, Float, Integer, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class Official(Base):
    __tablename__ = "officials"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    official_id: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    name: Mapped[str] = mapped_column(String(120))
    designation: Mapped[str] = mapped_column(String(120))
    jurisdiction: Mapped[str] = mapped_column(String(120))
    active: Mapped[bool] = mapped_column(Boolean, default=True)

class LandRecord(Base):
    __tablename__ = "land_records"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    survey_no: Mapped[str] = mapped_column(String(80), unique=True, index=True)
    owner_name: Mapped[str] = mapped_column(String(150))
    village: Mapped[str] = mapped_column(String(120))
    area_acres: Mapped[float] = mapped_column(Float)
    version: Mapped[int] = mapped_column(Integer, default=1)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

class Transaction(Base):
    __tablename__ = "transactions"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    tx_id: Mapped[str] = mapped_column(String(80), unique=True, index=True)
    survey_no: Mapped[str] = mapped_column(String(80), index=True)
    official_id: Mapped[str] = mapped_column(String(50), index=True)
    old_area: Mapped[float] = mapped_column(Float)
    new_area: Mapped[float] = mapped_column(Float)
    document_consistent: Mapped[bool] = mapped_column(Boolean)
    jurisdiction_match: Mapped[bool] = mapped_column(Boolean)
    login_security_anomaly: Mapped[bool] = mapped_column(Boolean)
    repeated_modifications: Mapped[int] = mapped_column(Integer, default=0)
    classical_risk: Mapped[float] = mapped_column(Float)
    quantum_risk: Mapped[float] = mapped_column(Float)
    combined_risk: Mapped[float] = mapped_column(Float)
    pqc_status: Mapped[str] = mapped_column(String(40))
    decision: Mapped[str] = mapped_column(String(40))
    status: Mapped[str] = mapped_column(String(40))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

class Alert(Base):
    __tablename__ = "alerts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    tx_id: Mapped[str] = mapped_column(String(80), index=True)
    recipient_type: Mapped[str] = mapped_column(String(40))
    recipient: Mapped[str] = mapped_column(String(150))
    message: Mapped[str] = mapped_column(Text)
    sent: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

class AuditEvent(Base):
    __tablename__ = "audit_events"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    tx_id: Mapped[str] = mapped_column(String(80), index=True)
    event_type: Mapped[str] = mapped_column(String(60))
    details: Mapped[str] = mapped_column(Text)
    previous_hash: Mapped[str] = mapped_column(String(64), default="")
    event_hash: Mapped[str] = mapped_column(String(64), index=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
