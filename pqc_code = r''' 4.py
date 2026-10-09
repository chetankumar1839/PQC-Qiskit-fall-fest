pqc_code = r'''
class PQCWrapper:

    def __init__(self):
        self.algorithm = "ML-DSA-65"

    def respond(self, risk):

        if risk > 0.50:
            return {
                "action": "BLOCK_AND_QUARANTINE",
                "status": "QUARANTINED",
                "message": "High-risk transaction blocked.",
                "algorithm": self.algorithm
            }

        elif risk > 0.30:
            return {
                "action": "ROTATE_KEYS",
                "status": "PQC_REESTABLISHED",
                "message": "Security keys rotated.",
                "algorithm": self.algorithm
            }

        else:
            return {
                "action": "MONITOR",
                "status": "MONITORING",
                "message": "Transaction allowed under normal monitoring.",
                "algorithm": self.algorithm
            }
'''

with open("backend/pqc_wrapper.py", "w") as f:
    f.write(pqc_code)

print("PQC Wrapper created successfully!")