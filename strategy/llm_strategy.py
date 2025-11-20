from .base_strategy import BaseStrategy
import requests
import json


class LLMStrategy(BaseStrategy):
    def __init__(self, api_key, model="gpt-4o-mini"):
        self.api_key = api_key
        self.model = model

    def score(self, m):
        if not self.api_key:
            return 0

        prompt = f"Predict probability direction:\n{m['question']}"
        # Implement actual LLM reasoning if user enables it.
        return 0
