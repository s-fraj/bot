from .momentum_strategy import MomentumStrategy
from .mean_reversion_strategy import MeanReversionStrategy
from .liquidity_aware_strategy import LiquidityAwareStrategy
from .llm_strategy import LLMStrategy
import numpy as np


class EnsembleStrategy:
    def __init__(self, client):
        cfg = client.config
        self.strategies = [
            MomentumStrategy(),
            MeanReversionStrategy(),
            LiquidityAwareStrategy(),
        ]
        if cfg.get("use_llm"):
            self.strategies.append(LLMStrategy(cfg["LLM_API_KEY"]))

    def decide(self, market):
        scores = [s.score(market) for s in self.strategies]
        weighted = np.mean(scores)
        return self.strategies[0].convert_score_to_action(weighted)
