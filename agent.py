from stock_tool import get_stock_analysis
from news_tool import get_recent_news
from sentiment_tool import analyze_news_sentiment


def run_stock_agent(ticker, start_date, end_date):

    data, technical_result = get_stock_analysis(
        ticker,
        start_date,
        end_date
    )

    if data is None:
        return None

    headlines = get_recent_news(ticker)

    sentiment_results, sentiment_summary = analyze_news_sentiment(
        headlines
    )

    final_signal, explanation = generate_final_decision(
        technical_result,
        sentiment_summary
    )

    result = {
        "data": data,
        "technical_result": technical_result,
        "sentiment_results": sentiment_results,
        "sentiment_summary": sentiment_summary,
        "final_signal": final_signal,
        "explanation": explanation
    }

    return result


def generate_final_decision(
    technical_result,
    sentiment_summary
):

    trend_signal = technical_result["trend_signal"]
    rsi_signal = technical_result["rsi_signal"]
    risk_level = technical_result["risk_level"]

    overall_sentiment = sentiment_summary[
        "overall_sentiment"
    ]

    if (
        trend_signal == "Bullish Trend"
        and rsi_signal != "Overbought"
        and risk_level != "High Risk"
        and overall_sentiment == "Positive"
    ):

        return (
            "Strong Watchlist Candidate",
            "Technical indicators and news sentiment are positive."
        )

    elif (
        trend_signal == "Bearish Trend"
        or overall_sentiment == "Negative"
    ):

        return (
            "High Risk / Be Careful",
            "The stock trend or news sentiment shows warning signs."
        )

    else:

        return (
            "Need More Confirmation",
            "Signals are mixed and need more confirmation."
        )