import yfinance as yf
import pandas as pd


def convert_ticker(ticker):

    ticker = str(ticker).strip()

    if ticker.isdigit():
        return f"{ticker}.TW"

    return ticker.upper()


def get_market_movers(tickers, period="5d"):

    results = []

    for ticker in tickers:

        yf_ticker = convert_ticker(ticker)

        try:

            data = yf.download(
                yf_ticker,
                period=period,
                progress=False
            )

            if data.empty or len(data) < 2:
                continue

            if isinstance(data.columns, pd.MultiIndex):
                data.columns = data.columns.get_level_values(0)

            first_close = float(data["Close"].iloc[0])
            last_close = float(data["Close"].iloc[-1])

            change_pct = (
                (last_close - first_close)
                / first_close
            ) * 100

            results.append({
                "Ticker": ticker,
                "Change %": round(change_pct, 2),
                "Latest Price": round(last_close, 2)
            })

        except Exception:
            continue

    df = pd.DataFrame(results)

    if df.empty:
        return df, df

    gainers = df.sort_values(
        "Change %",
        ascending=False
    ).head(5)

    losers = df.sort_values(
        "Change %",
        ascending=True
    ).head(5)

    return gainers, losers