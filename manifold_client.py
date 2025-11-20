import requests
import json
from loguru import logger


class ManifoldClient:
    BASE = "https://api.manifold.markets/v0"

    def __init__(self, config_path="config.json"):
        with open(config_path) as f:
            cfg = json.load(f)
        self.api_key = cfg["API_KEY"]

    def _auth(self):
        return {"Authorization": f"Key {self.api_key}"}

    def get_open_markets(self):
        r = requests.get(f"{self.BASE}/markets?limit=200")
        r.raise_for_status()
        return r.json()

    def execute_trade(self, market, action):
        payload = {
            "contractId": market["id"],
            "amount": action["amount"],
            "outcome": action["outcome"],
        }
        r = requests.post(f"{self.BASE}/bet", json=payload, headers=self._auth())
        r.raise_for_status()
        logger.info(f"Placed trade: {payload}")
        return r.json()
