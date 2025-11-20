from .base_strategy import BaseStrategy
import numpy as np


class MeanReversionStrategy(BaseStrategy):
    def score(self, m):
        hist = m.get("probabilityHistory", [])
        if len(hist) < 20:
            return 0

        last = hist[-1]
        avg = np.mean(hist[-20:])

        return float(avg - last)
