import os

os.makedirs("backend", exist_ok=True)

print("Backend folder created successfully!")
%%writefile backend/quantum_risk.py

import math
import numpy as np

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator


def calculate_quantum_risk(features):

    x = np.clip(
        np.array(features, dtype=float),
        0.0,
        1.0
    )

    qc = QuantumCircuit(3, 1)

    # Encode risk features
    qc.ry(math.pi * x[0], 0)
    qc.ry(math.pi * x[1], 1)
    qc.ry(math.pi * x[2], 2)

    # Entanglement
    qc.cx(0, 2)
    qc.cx(1, 2)

    # Combine features
    qc.ry(math.pi * np.mean(x), 2)

    # Measure
    qc.measure(2, 0)

    simulator = AerSimulator()

    compiled_circuit = transpile(qc, simulator)

    result = simulator.run(
        compiled_circuit,
        shots=512
    ).result()

    counts = result.get_counts()

    ones = counts.get("1", 0)

    quantum_risk = ones / 512

    return {
        "quantum_risk": quantum_risk,
        "quantum_risk_percentage": round(
            quantum_risk * 100, 2
        ),
        "counts": counts,
        "circuit": qc.draw("text")
    }