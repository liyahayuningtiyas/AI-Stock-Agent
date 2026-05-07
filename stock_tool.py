import yfinance as yf
import pandas as pd


def get_stock_analysis(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)

    if data.empty:
        return None, None

    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    data = data.ffill().bfill()

    data["MA20"] = data["Close"].rolling(window=20).mean()
    data["MA50"] = data["Close"].rolling(window=50).mean()
    data["Daily_Return"] = data["Close"].pct_change()

    delta = data["Close"].diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.rolling(window=14).mean()
    avg_loss = loss.rolling(window=14).mean()

    rs = avg_gain / avg_loss
    data["RSI"] = 100 - (100 / (1 + rs))

    data["Volatility_20"] = data["Daily_Return"].rolling(window=20).std()

    data = data.dropna()

    latest = data.iloc[-1]

    close_price = float(latest["Close"])
    ma20 = float(latest["MA20"])
    ma50 = float(latest["MA50"])
    rsi = float(latest["RSI"])
    volatility = float(latest["Volatility_20"])

    if close_price > ma20 and ma20 > ma50:
        trend_signal = "Bullish Trend"
    elif close_price < ma20 and ma20 < ma50:
        trend_signal = "Bearish Trend"
    else:
        trend_signal = "Mixed / Uncertain Trend"

    if rsi > 70:
        rsi_signal = "Overbought"
    elif rsi < 30:
        rsi_signal = "Oversold"
    else:
        rsi_signal = "Neutral"

    if volatility > 0.04:
        risk_level = "High Risk"
    elif volatility > 0.02:
        risk_level = "Medium Risk"
    else:
        risk_level = "Low Risk"

    technical_result = {
        "close_price": close_price,
        "ma20": ma20,
        "ma50": ma50,
        "rsi": rsi,
        "volatility": volatility,
        "trend_signal": trend_signal,
        "rsi_signal": rsi_signal,
        "risk_level": risk_level,
    }

    return data, technical_result