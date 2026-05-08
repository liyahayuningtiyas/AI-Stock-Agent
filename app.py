import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from agent import run_stock_agent
from market_movers import get_market_movers

st.set_page_config(
    page_title="AI Stock Agent",
    layout="wide"
)

st.title("AI Stock Agent Dashboard")

st.write("This app analyzes stock trends, risk, and recent news sentiment.")

st.sidebar.title("Control Panel")

ticker_input = st.sidebar.text_input(
    "Enter Stock Ticker or Taiwan Stock Number",
    "2330"
)

# Auto convert Taiwan stock number
if ticker_input.isdigit():
    ticker = f"{ticker_input}.TW"
else:
    ticker = ticker_input.upper()

start_date = st.sidebar.date_input(
    "Start Date",
    pd.to_datetime("2025-01-01")
)

end_date = st.sidebar.date_input(
    "End Date",
    pd.to_datetime("2026-01-01")
)

analyze_button = st.sidebar.button("Analyze Stock")

st.subheader("Market Overview")

st.caption(
    "Market performance overview based on selected watchlist stocks."
)

watchlist = [
    "2330",
    "2454",
    "2303",
    "2379",
    "8299",
    "NVDA",
    "AAPL",
    "MSFT",
    "AMD",
    "TSM",
    "TSLA",
    "GOOGL",
    "META",
    "BTC-USD",
    "ETH-USD"
]

gainers, losers = get_market_movers(
    watchlist,
    period="5d"
)

market_df = pd.concat([gainers, losers])

market_df = market_df.drop_duplicates()

market_df = market_df.sort_values(
    "Change %",
    ascending=False
)

def market_status(change):

    if change > 3:
        return "🚀 Strong Up"

    elif change > 0:
        return "🟢 Up"

    elif change < -3:
        return "🔻 Strong Down"

    else:
        return "🔴 Down"

market_df["Status"] = market_df["Change %"].apply(
    market_status
)

st.dataframe(
    market_df,
    use_container_width=True
)

col_g, col_l = st.columns(2)

with col_g:
    st.markdown("### 🚀 Top Gainers")
    st.dataframe(
        gainers,
        use_container_width=True
    )

with col_l:
    st.markdown("### 📉 Top Losers")
    st.dataframe(
        losers,
        use_container_width=True
    )
if analyze_button:

    result = run_stock_agent(ticker, start_date, end_date)

    if result is None:
        st.error("No data found. Please check the ticker symbol.")

    else:
        data = result["data"]
        tech = result["technical_result"]
        sentiment_results = result["sentiment_results"]
        sentiment_summary = result["sentiment_summary"]

        st.subheader("Latest Analysis")

        col1, col2, col3, col4, col5 = st.columns(5)

        col1.metric("Close Price", f"{tech['close_price']:.2f}")
        col2.metric("MA20", f"{tech['ma20']:.2f}")
        col3.metric("MA50", f"{tech['ma50']:.2f}")
        col4.metric("RSI", f"{tech['rsi']:.2f}")
        col5.metric("Risk Level", tech["risk_level"])

        st.info(f"Trend Signal: {tech['trend_signal']}")
        st.warning(f"RSI Signal: {tech['rsi_signal']}")

        st.subheader("Final AI Agent Decision")
        st.success(f"Final Signal: {result['final_signal']}")
        st.write(result["explanation"])
        
        st.subheader("Agent Report")

        report_text = f"""
        ### Stock: {ticker}

        **Technical Trend:** {tech['trend_signal']}  
        **RSI Condition:** {tech['rsi_signal']}  
        **Risk Level:** {tech['risk_level']}  
        **News Sentiment:** {sentiment_summary['overall_sentiment']}  

        **Final Agent Decision:** {result['final_signal']}

        **Explanation:**  
        {result['explanation']}

        **Important Note:**  
        This is a decision-support system, not financial advice. The stock market is uncertain, and investors should consider additional research before making decisions.
        """

        st.markdown(report_text)

        st.subheader("Interactive Candlestick Chart")

        fig = go.Figure()

        fig.add_trace(go.Candlestick(
            x=data.index,
            open=data["Open"],
            high=data["High"],
            low=data["Low"],
            close=data["Close"],
            name="Candlestick"
        ))

        fig.add_trace(go.Scatter(
            x=data.index,
            y=data["MA20"],
            mode="lines",
            name="MA20"
        ))

        fig.add_trace(go.Scatter(
            x=data.index,
            y=data["MA50"],
            mode="lines",
            name="MA50"
        ))

        fig.update_layout(
            title=f"{ticker} Candlestick Chart",
            xaxis_title="Date",
            yaxis_title="Price",
            hovermode="x unified",
            height=600,
            xaxis_rangeslider_visible=False
        )

        st.plotly_chart(fig, use_container_width=True)

        st.subheader("RSI Chart")

        fig_rsi, ax_rsi = plt.subplots(figsize=(12, 4))

        ax_rsi.plot(data.index, data["RSI"], label="RSI")
        ax_rsi.axhline(70, linestyle="--", label="Overbought 70")
        ax_rsi.axhline(30, linestyle="--", label="Oversold 30")

        ax_rsi.set_title(f"{ticker} RSI Indicator")
        ax_rsi.set_xlabel("Date")
        ax_rsi.set_ylabel("RSI")
        ax_rsi.legend()
        ax_rsi.grid(True)

        st.pyplot(fig_rsi)

        st.subheader("Recent News & AI Sentiment")

        for item in sentiment_results:
            label = item["label"]
            headline = item["headline"]
            confidence = item["confidence"]

            if label == "positive":
                emoji = "🟢"
            elif label == "negative":
                emoji = "🔴"
            else:
                emoji = "🟡"

            st.write(f"{emoji} {headline}")
            st.caption(f"Sentiment: {label} | Confidence: {confidence:.2f}")

        st.subheader("AI News Summary")

        st.write(f"🟢 Positive News: {sentiment_summary['positive_count']}")
        st.write(f"🔴 Negative News: {sentiment_summary['negative_count']}")
        st.write(f"🟡 Neutral News: {sentiment_summary['neutral_count']}")
        st.success(f"Overall News Sentiment: {sentiment_summary['overall_sentiment']}")

        st.subheader("Recent Stock Data")
        st.dataframe(data.tail(20))