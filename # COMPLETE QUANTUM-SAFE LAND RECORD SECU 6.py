# COMPLETE QUANTUM-SAFE LAND RECORD SECURITY PIPELINE

from backend.quantum_risk import calculate_quantum_risk
from backend.pqc_wrapper import PQCWrapper


def process_land_transaction(
    area_change_risk,
    document_risk,
    login_risk
):

    print("====================================")
    print(" LAND RECORD SECURITY SYSTEM")
    print("====================================")

    # --------------------------------
    # 1. AI / Classical risk features
    # --------------------------------

    print("\n[1] AI Risk Analysis")

    classical_risk = (
        area_change_risk +
        document_risk +
        login_risk
    ) / 3

    print(
        f"Classical Risk: "
        f"{classical_risk * 100:.2f}%"
    )

    # --------------------------------
    # 2. Qiskit quantum processing
    # --------------------------------

    print("\n[2] Qiskit Quantum Processing")

    quantum_result = calculate_quantum_risk([
        area_change_risk,
        document_risk,
        login_risk
    ])

    quantum_risk = quantum_result["quantum_risk"]

    print(
        f"Quantum Risk: "
        f"{quantum_risk * 100:.2f}%"
    )

    # --------------------------------
    # 3. Combine risks
    # --------------------------------

    combined_risk = (
        0.70 * classical_risk +
        0.30 * quantum_risk
    )

    print("\n[3] Combined Risk")

    print(
        f"Combined Risk: "
        f"{combined_risk * 100:.2f}%"
    )

    # --------------------------------
    # 4. PQC Wrapper
    # --------------------------------

    print("\n[4] PQC Security Response")

    wrapper = PQCWrapper()

    response = wrapper.respond(combined_risk)

    print("Action:", response["action"])
    print("Status:", response["status"])
    print("Algorithm:", response["algorithm"])

    print("\nMessage:")
    print(response["message"])

    print("\n====================================")

    return {
        "classical_risk": classical_risk,
        "quantum_risk": quantum_risk,
        "combined_risk": combined_risk,
        "pqc_response": response
    }