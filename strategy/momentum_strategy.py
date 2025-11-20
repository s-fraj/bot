from .base_strategy import BaseStrategy
import numpy as np


class MomentumStrategy(BaseStrategy):
    def score(self, m):
        hist = m.get("probabilityHistory", [])
        if len(hist) < 10:
            return 0
        return float(hist[-1] - hist[-10])
