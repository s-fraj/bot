from .base_strategy import BaseStrategy


class LiquidityAwareStrategy(BaseStrategy):
    def score(self, m):
        depth = m.get("totalLiquidity", 0)
        if depth < 50:
            return -0.2
        if depth > 1000:
            return 0.1
        return 0
