import numpy as np
from sklearn.ensemble import IsolationForest

class ActivityMonitor:
    """
    Hackathon prototype:
    - Uses transparent rule-based signals for explainability.
    - Also fits an Isolation Forest on a small synthetic baseline so the
      architecture can later be replaced with real historical activity data.
    """
    def __init__(self):
        baseline = np.array([
            [0.02, 0, 1, 1, 0],
            [0.05, 0, 1, 1, 0],
            [0.08, 1, 1, 1, 0],
            [0.03, 0, 1, 1, 1],
            [0.10, 1, 1, 1, 0],
            [0.07, 0, 1, 1, 0],
            [0.04, 0, 1, 1, 0],
            [0.12, 1, 1, 1, 0],
        ])
        self.model = IsolationForest(contamination=0.15, random_state=42)
        self.model.fit(baseline)

    def score(self, old_area, new_area, document_consistent,
              jurisdiction_match, login_security_anomaly,
              repeated_modifications):
        change_ratio = abs(new_area - old_area) / max(old_area, 0.01)

        # Explainable prototype score.
        risk = 0.0
        reasons = []

        if change_ratio > 0.50:
            risk += 0.25
            reasons.append("large area change")
        elif change_ratio > 0.20:
            risk += 0.12
            reasons.append("unusual area change")

        if not document_consistent:
            risk += 0.20
            reasons.append("document inconsistency")

        if not jurisdiction_match:
            risk += 0.15
            reasons.append("jurisdiction mismatch")

        if login_security_anomaly:
            risk += 0.15
            reasons.append("abnormal login/session behavior")

        if repeated_modifications >= 3:
            risk += 0.15
            reasons.append("repeated modifications")

        risk = min(risk, 1.0)
        return round(risk, 4), reasons
