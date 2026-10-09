import os

os.makedirs("backend", exist_ok=True)

code = r'''
import math
import numpy as np

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator


def calculate_quantum_risk(features):

    # Keep values between 0 and 1
    x = np.clip(
        np.array(features, dtype=float),
        0.0,
        1.0
    )

    # Create 3-qubit quantum circuit
    qc = QuantumCircuit(3, 1)

    # Encode the three risk features
    qc.ry(math.pi * x[0], 0)
    qc.ry(math.pi * x[1], 1)
    qc.ry(math.pi * x[2], 2)

    # Entangle qubits
    qc.cx(0, 2)
    qc.cx(1, 2)

    # Combine the risk features
    qc.ry(math.pi * np.mean(x), 2)

    # Measure the third qubit
    qc.measure(2, 0)

    # Qiskit Aer simulator
    simulator = AerSimulator()

    compiled_circuit = transpile(
        qc,
        simulator
    )

    result = simulator.run(
        compiled_circuit,
        shots=512
    ).result()

    counts = result.get_counts()

    # Number of times we measured |1>
    ones = counts.get("1", 0)

    # Quantum risk probability
    quantum_risk = ones / 512

    return {
        "quantum_risk": quantum_risk,
        "quantum_risk_percentage": round(
            quantum_risk * 100,
            2
        ),
        "counts": counts,
        "circuit": qc.draw("text")
    }
'''

with open("backend/quantum_risk.py", "w") as f:
    f.write(code)

print("quantum_risk.py created successfully!")
import os

print(os.path.exists("backend/quantum_risk.py"))
import os

print(os.path.exists("backend/quantum_risk.py"))
from backend.quantum_risk import calculate_quantum_risk

result = calculate_quantum_risk([
    0.8,   # area-change risk
    1.0,   # document risk
    0.6    # login risk
])

print("Quantum Risk:", result["quantum_risk_percentage"], "%")

print("\nMeasurement Counts:")
print(result["counts"])

print("\nQuantum Circuit:")
print(result["circuit"])