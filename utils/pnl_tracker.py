from datetime import datetime
import os


class PnLTracker:
    def __init__(self):
        self.trades = []

    def record_trade(self, trade):
        self.trades.append(trade)

    def generate_daily_report(self):
        if not self.trades:
            return

        today = datetime.now().strftime("%Y-%m-%d")
        path = f"reports/daily-report-{today}.md"
        os.makedirs("reports", exist_ok=True)

        pnl = sum(t.get("profit", 0) for t in self.trades)

        with open(path, "w") as f:
            f.write(f"# Daily Report {today}\n")
            f.write(f"Total PnL: {pnl}\n")

        self.trades = []
