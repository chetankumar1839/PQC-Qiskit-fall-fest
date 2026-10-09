import hashlib
import json
import os
from datetime import datetime

DEMO_MODE = os.getenv("DEMO_MODE", "1") == "1"

class PQCWrapper:
    """
    Demo wrapper for the hackathon.
    In DEMO_MODE it simulates PQC verification/rotation.
    For a production-style demo, connect a supported ML-DSA implementation.
    """

    algorithm = "ML-DSA-65"

    def verify_and_respond(self, risk):
        if risk > 0.50:
            return {
                "status": "VERIFIED-DEMO",
                "action": "BLOCK_AND_QUARANTINE",
                "algorithm": self.algorithm,
            }
        if risk > 0.30:
            return {
                "status": "VERIFIED-DEMO",
                "action": "ROTATE_KEYS",
                "algorithm": self.algorithm,
            }
        return {
            "status": "VERIFIED-DEMO",
            "action": "MONITOR",
            "algorithm": self.algorithm,
        }

    def demo_signature(self, payload):
        # Demonstration fingerprint only; NOT a cryptographic signature.
        raw = json.dumps(payload, sort_keys=True).encode()
        return hashlib.sha256(raw).hexdigest()
