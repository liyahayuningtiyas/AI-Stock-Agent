import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from agent import run_stock_agent

st.set_page_config(
    page_title="AI Stock Agent",
    layout="wide"
)

st.title("AI Stock Agent Dashboard")
st.write("This app analyzes stock trends, risk, and recent news sentiment.")

ticker = st.text_input("Enter stock ticker", "TSM")

start_date = st.date_input("Start date", pd.to_datetime("2025-01-01"))
end_date = st.date_input("End date", pd.to_datetime("2026-01-01"))

if st.button("Analyze Stock"):

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

        st.subheader("Stock Chart")

        fig, ax = plt.subplots(figsize=(12, 5))

        ax.plot(data.index, data["Close"], label="Close Price")
        ax.plot(data.index, data["MA20"], label="MA20")
        ax.plot(data.index, data["MA50"], label="MA50")

        ax.set_title(f"{ticker} Stock Analysis")
        ax.set_xlabel("Date")
        ax.set_ylabel("Price")
        ax.legend()
        ax.grid(True)

        st.pyplot(fig)

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