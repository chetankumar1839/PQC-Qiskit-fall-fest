# Quantum-Safe Land Record Security — Qiskit Fall Fest Prototype

## Goal
Prototype the hackathon use case "Quantum-safe DLT for land records and supply chains" with:
- central AI monitoring of authorized officials
- Qiskit quantum risk signal
- PQC security controller/wrapper
- block/quarantine + alerts for high-risk transactions
- SQLite database
- tamper-evident hash-chain audit trail
- web dashboard

## Architecture
Frontend (HTML/CSS/JS)
        |
        v
FastAPI backend
        |
        +--> SQLite database
        +--> AI activity monitor
        +--> Qiskit quantum risk circuit
        +--> PQC wrapper
        +--> audit hash chain

## Risk policy
- 0–30%: allow + monitor
- >30–50%: rotate cryptographic keys / re-establish PQC
- >50%: block + quarantine + alert landowner and relevant supervisor

The AI detects suspicious activity; it does not declare an official guilty.

## Run locally
```bash
pip install -r requirements.txt
uvicorn backend.main:app --reload
```
Open http://127.0.0.1:8000

## Google Colab
Upload/extract the project, then run:
```python
!pip install -r requirements.txt
!uvicorn backend.main:app --host 0.0.0.0 --port 8000 &
```
For a public temporary demo URL, use a tunneling service approved by your event environment. Do not expose real personal land data.

## Demo high-risk transaction
Survey 145/2, official OFF-1047:
- New area: 6.50
- Document consistent: OFF
- Jurisdiction match: OFF
- Login/session anomaly: ON
- Repeated modifications: 5

This should produce a high-risk response and demonstrate block/quarantine + alerts.

## Important technical note
The Qiskit module is a quantum risk-processing demonstration. It does not itself provide post-quantum cryptographic security. PQC handles cryptographic protection, while the audit ledger provides tamper-evident history.

The current PQC wrapper is a demo controller. Before a real security deployment, replace demo verification with a vetted ML-DSA implementation and conduct proper security review.
