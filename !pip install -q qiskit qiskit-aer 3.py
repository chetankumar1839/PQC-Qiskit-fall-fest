!pip install -q qiskit qiskit-aer
import qiskit
import qiskit_aer

print("Qiskit:", qiskit.__version__)
print("Qiskit Aer:", qiskit_aer.__version__)
from backend.quantum_risk import calculate_quantum_risk

result = calculate_quantum_risk([
    0.8,
    1.0,
    0.6
])

print("Quantum Risk:", result["quantum_risk_percentage"], "%")

print("\nMeasurement Counts:")
print(result["counts"])

print("\nQuantum Circuit:")
print(result["circuit"])