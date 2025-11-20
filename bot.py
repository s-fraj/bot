from api_wrapper import ManifoldAPIWrapper
from strategy import simple_strategy

def main():
    api_key = "YOUR_BOT_API_KEY"
    bot = ManifoldAPIWrapper(api_key)

    # Fetch active markets created by MikhailTal
    markets = bot.get_markets_by_creator("MikhailTal")
    print(f"Active markets by MikhailTal: {len(markets)}")

    for market in markets:
        # Decide whether and how to bet
        bet = simple_strategy(market)
        if bet:
            outcome, amount = bet
            success = bot.place_bet(market['id'], amount, outcome)
            if success:
                print(f"Placed {outcome} bet of {amount} on {market['question']}")
            else:
                print(f"Failed to bet on {market['question']}")

if __name__ == "__main__":
    main()
