import requests

class ManifoldAPIWrapper:
    BASE_URL = "https://api.manifold.markets/v0"

    def __init__(self, api_key):
        self.api_key = api_key
        self.headers = {"Authorization": f"Key {self.api_key}"}

    def get_markets_by_creator(self, creator_username):
        url = f"{self.BASE_URL}/markets?userId={creator_username}&limit=100"
        response = requests.get(url)
        if response.ok:
            markets = response.json()
            return [m for m in markets if not m.get('isResolved', False)]
        return []

    def place_bet(self, market_id, amount, outcome):
        url = f"{self.BASE_URL}/bet"
        data = {"contractId": market_id, "amount": amount, "outcome": outcome}
        response = requests.post(url, headers=self.headers, json=data)
        return response.ok
