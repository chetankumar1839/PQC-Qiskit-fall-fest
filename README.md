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
  
AI-Integrated Quantum-Safe Land Record Protection System

AI + Qiskit + Post-Quantum Cryptography + Tamper-Evident Audit Trail

1. Project Overview

This project proposes a security framework for protecting digital land records against unauthorized modifications, compromised accounts, suspicious official activity, and future quantum-computing threats.

It combines classical AI-based risk analysis, Qiskit quantum circuit simulation, post-quantum cryptography (PQC), and a tamper-evident audit trail.

2. Problem Statement

Digital land records may be affected by unauthorized changes, compromised credentials, document inconsistencies, and misuse of authorized accounts. Authentication alone cannot determine whether every transaction is legitimate.

Our system analyzes transaction behavior, calculates risk, applies configurable security responses, and records events for auditing.

3. Objectives

- Detect suspicious land-record changes.
- Analyze transaction risks using classical and experimental quantum processing.
- Design a PQC-based transaction-signature workflow.
- Apply adaptive security responses.
- Maintain a traceable audit history.
- Benchmark the hybrid system against a classical baseline.

4. System Architecture

flowchart TD
    A[Land Documents] --> B[Digitization and Validation]
    B --> C[Historical Record Database]
    D[Official Proposes Change] --> E[Transaction Validation]
    C --> E
    E --> F[Risk Feature Extraction]
    F --> G[Classical AI Risk Analysis]
    F --> H[Qiskit Circuit Simulation]
    G --> I[Combined Risk Score]
    H --> I
    I --> J{Security Controller}
    J -->|0–30%| K[Monitor and Log]
    J -->|Above 30–50%| L[Key Rotation Workflow]
    J -->|Above 50%| M[Block and Quarantine]
    L --> N[Alerts and Audit Trail]
    K --> N
    M --> O[Notify Owner and Supervisor]
    O --> P[Human Verification]
    P --> N

5. How the System Works

1. Digitization: Physical documents are scanned and relevant data is extracted using OCR, followed by validation.
2. Transaction submission: An authorized official proposes a change to a land record.
3. Feature extraction: The system checks area changes, document inconsistencies, historical conflicts, and unusual activity.
4. Classical risk analysis: A classical model evaluates the transaction's risk indicators.
5. Qiskit processing: A simulated quantum circuit encodes selected features, applies quantum gates and entanglement, and measures an output.
6. Risk fusion: Classical and quantum-component outputs contribute to a combined risk score.
7. Security response: A controller applies the configured response based on the score.
8. Alerting: Suspicious transactions are flagged for review by the landowner and relevant supervisory official.
9. Audit trail: Events are recorded in a hash-linked log to help detect tampering.

6. Risk-Based Security Policy

Risk score| Response
0–30%| Continue monitoring and logging
Above 30% to 50%| Initiate key rotation and renew the secure session
Above 50%| Block and quarantine the proposed transaction; alert responsible parties and require human verification

These are prototype thresholds, not universal security standards. Key rotation and algorithm switching are different operations.

7. Technology Stack

- Python
- Qiskit and Qiskit Aer
- Classical AI and risk analysis
- Post-Quantum Cryptography
- FastAPI
- SQLite
- HTML, CSS, and JavaScript
- Hash-chain audit logging

Implementation note: ML-DSA-65 should be described as implemented only after real key generation, signing, and verification have been integrated and tested. A hash fingerprint alone is not an ML-DSA signature.

8. Repository Structure

quantum-safe-land-records/
├── backend/
│   ├── main.py
│   ├── models.py
│   ├── database.py
│   ├── ai_monitor.py
│   ├── quantum_risk.py
│   ├── pqc_wrapper.py
│   └── ledger.py
├── frontend/
│   └── index.html
├── data/
├── requirements.txt
├── .gitignore
└── README.md

Update this structure to match the files actually uploaded to your repository.

9. Setup and Execution

Install Python and Git, then clone the repository:

git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
cd YOUR-REPOSITORY
python -m venv .venv

Activate the environment.

Windows:

.venv\Scripts\activate

macOS/Linux:

source .venv/bin/activate

Install dependencies and run the prototype:

pip install -r requirements.txt
uvicorn backend.main:app --reload

Open "http://127.0.0.1:8000" in your browser. Adjust the command if the actual project entry point differs.

10. Testing and Benchmarking

Use labeled normal and suspicious transactions to evaluate:

- Accuracy, precision, recall, and F1-score.
- False-positive and false-negative rates.
- Confusion matrix.
- Execution time.
- Qiskit simulation variability.
- Valid-signature verification and modified-data rejection after real PQC signing is integrated.

Compare classical and hybrid approaches using the same test cases. Publish measured results rather than assumed improvements.

11. Security Considerations

- Use synthetic demo records in the public repository.
- Never upload private keys, passwords, tokens, or real landowner data.
- A valid signature does not prove that a transaction is legally correct.
- Require human review for high-risk cases.
- Production deployment requires secure key management, authentication, backups, privacy review, and independent security testing.

12. Limitations and Future Scope

This is an educational hackathon prototype, not a production land registry. Future work includes real ML-DSA integration, validated OCR, stronger AI evaluation, secure key storage, permissioned DLT integration, and reproducible benchmarking.

No quantum advantage is claimed until experiments demonstrate an improvement over a suitable classical baseline.

Team Information

- Team name: Qubexa
- Team members: B.Chetan Kumar
-               k.Dhanu Sri
-               k.Siddhardha
- Event: IBM Qiskit Fall Fest
- Repository: Add your public GitHub URL

Disclaimer: This project is an educational prototype and is not a certified security product or legal land-record system.

## Important technical note
The Qiskit module is a quantum risk-processing demonstration. It does not itself provide post-quantum cryptographic security. PQC handles cryptographic protection, while the audit ledger provides tamper-evident history.

The current PQC wrapper is a demo controller. Before a real security deployment, replace demo verification with a vetted ML-DSA implementation and conduct proper security review.
