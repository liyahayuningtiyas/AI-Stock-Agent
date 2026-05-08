# AI Stock Agent Dashboard

![Dashboard](dashboard.png)

## Overview

AI Stock Agent Dashboard is an AI-assisted financial analysis platform developed using Python and Streamlit. The project combines technical analysis, market monitoring, sentiment analysis, and interactive visualization into a single dashboard system.

The purpose of this project is to explore how AI-based workflows and intelligent decision-support systems can assist traders and investors in understanding stock market conditions more effectively.

Unlike many complex trading platforms, this project focuses on creating a dashboard that is:

* User-friendly
* Interactive
* Practical for beginners and part-time traders
* Flexible for future AI-agent integration
* Easy to expand into larger intelligent systems

This project is currently being developed as part of my self-learning journey in AI systems, software engineering, and financial intelligence.

---

# Key Features

## Technical Analysis

The dashboard supports:

* Moving Average (MA20 / MA50)
* Relative Strength Index (RSI)
* Risk level evaluation
* Trend signal analysis
* Candlestick visualization

---

## Market Overview

The dashboard includes a market overview section inspired by financial platforms such as:

* TradingView
* Binance
* Yahoo Finance
* CoinMarketCap

Users can monitor:

* Market gainers
* Market losers
* Watchlist performance
* Percentage price changes

---

## Taiwan & Global Stock Support

The system supports:

### Taiwan Stocks

Examples:

* 2330 (TSMC)
* 2454 (MediaTek)
* 2303 (UMC)

The dashboard automatically converts Taiwan stock numbers into Yahoo Finance format.

Example:

```python
2330 -> 2330.TW
```

### US Stocks & Crypto

Examples:

* NVDA
* AAPL
* TSLA
* BTC-USD
* ETH-USD

---

## AI News Sentiment Analysis

The dashboard collects recent financial news and performs sentiment analysis to classify news into:

* Positive
* Neutral
* Negative

This helps users quickly understand the overall market sentiment surrounding a stock.

---

## Agent Report System

The dashboard generates a simplified AI-style report that summarizes:

* Technical trend
* RSI condition
* Risk level
* News sentiment
* Final AI decision

The goal is to simulate an intelligent financial assistant capable of supporting investment decision-making.

---

# System Architecture

```text
User Input
    ↓
Streamlit Dashboard
    ↓
Agent System
    ↓
┌───────────────────────┐
│ stock_tool.py         │
│ news_tool.py          │
│ sentiment_tool.py     │
│ market_movers.py      │
└───────────────────────┘
    ↓
AI Decision & Visualization
```

---

# Technologies Used

| Technology   | Purpose                      |
| ------------ | ---------------------------- |
| Python       | Core programming language    |
| Streamlit    | Interactive dashboard UI     |
| Plotly       | Interactive financial charts |
| Pandas       | Data analysis                |
| yFinance     | Stock market data            |
| Matplotlib   | RSI visualization            |
| Git & GitHub | Version control              |

---

# Project Structure

```text
AI-Stock-Agent/
│
├── app.py
├── agent.py
├── stock_tool.py
├── news_tool.py
├── sentiment_tool.py
├── market_movers.py
├── requirements.txt
├── README.md
└── dashboard.png
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/liyahayuningtiyas/AI-Stock-Agent.git
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

Activate:

### macOS / Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run Application

```bash
streamlit run app.py
```

Then open:

```text
http://localhost:8501
```

---

# Future Development

This project is still in the early development stage. Planned future improvements include:

* OpenAI API integration
* AI-generated financial summaries
* Multi-agent architecture
* LSTM / deep learning prediction models
* Portfolio tracking system
* Database integration
* Cloud deployment
* Real-time notification system
* Advanced trading indicators
* Interactive dark-mode financial UI

---

# Learning Journey

This project represents my transition from an MBA background into AI systems and software engineering.

During development, I explored:

* Python application architecture
* Streamlit dashboard engineering
* Financial data analysis
* Git/GitHub workflow
* Interactive visualization
* AI-agent design concepts

The project is not intended to provide financial advice. Instead, it serves as a learning platform for exploring intelligent financial systems and AI-assisted decision support.

---

# Disclaimer

This project is for educational and research purposes only.

The dashboard does not provide financial advice, and investment decisions should always involve additional research and risk evaluation.

---

# Author

Liya Hayuningtiyas

MBA → AI / Engineering Transition Journey

National Cheng Kung University (NCKU)
School of Electrical Engineering and Computer Science

GitHub:
[https://github.com/liyahayuningtiyas](https://github.com/liyahayuningtiyas)
