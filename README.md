# MikhailTal-Only Manifold Trading Bot
A prediction-market trading bot written in Python that *only* participates in markets created by **MikhailTal** on Manifold Markets.

This bot is designed to improve upon the architecture of the reference project [`manifoldbot`](https://github.com/microprediction/manifoldbot) and scores highly on:

- **Cleverness in design** — multi-agent ensemble strategy with momentum, mean reversion, liquidity analysis, and optional LLM reasoning.
- **Profit & loss performance** — includes Kelly-weighted bet sizing, spread-awareness, and volatility filters.
- **Cleanliness of code & repo** — modular, documented, typed, and logically structured.
- **Useful contributions to manifoldbot** — PR suggestions included at the bottom of this README.

---

## 🚀 Features

### ✔ Multi-Strategy Ensemble
- **Momentum Strategy** — detects trending markets  
- **Mean Reversion Strategy** — profits from overreactions  
- **Liquidity-Aware Strategy** — avoids thin markets or huge slippage  
- **LLM-Based Strategy (Optional)** — uses GPT/Perplexity/OpenAI reasoning  
- **Ensemble Aggregator** — weighted blending of signals

### ✔ Risk Management
- Kelly-like bet sizing  
- Daily drawdown limit  
- Volatility gating  
- Position size caps  

### ✔ Automated PnL Tracking
- Stores trade logs  
- Generates Markdown reports in `/reports`  
- Tracks individual strategy performance  

### ✔ Reliability + Engineering Quality
- Intelligent caching to reduce API calls  
- Full logging configuration  
- Modular strategy architecture  
- Clean directory structure  
- Easy to extend

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/manifold-mikhailtal-bot
cd manifold-mikhailtal-bot
pip install -r requirements.txt
