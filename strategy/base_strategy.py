class BaseStrategy:
    def score(self, market):
        raise NotImplementedError

    def convert_score_to_action(self, score):
        if abs(score) < 0.1:
            return None
        amount = min(50, max(5, abs(score) * 100))
        return {
            "outcome": "YES" if score > 0 else "NO",
            "amount": amount
        }
