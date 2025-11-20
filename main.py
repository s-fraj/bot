from manifold_client import ManifoldClient
from strategy.ensemble import EnsembleStrategy
from utils.market_filters import is_mikhailtal_market
from utils.logging_config import setup_logging
from utils.pnl_tracker import PnLTracker
import time
from loguru import logger


def main():
    setup_logging()
    client = ManifoldClient("config.json")
    strategy = EnsembleStrategy(client)
    pnl_tracker = PnLTracker()

    logger.info("Starting MikhailTal-only trading bot.")

    while True:
        markets = client.get_open_markets()

        for m in markets:
            if not is_mikhailtal_market(m):
                continue

            rec = strategy.decide(m)
            if rec is None:
                continue

            result = client.execute_trade(m, rec)
            pnl_tracker.record_trade(result)

        pnl_tracker.generate_daily_report()
        time.sleep(60)


if __name__ == "__main__":
    main()
