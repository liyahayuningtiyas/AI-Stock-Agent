def analyze_news_sentiment(headlines):

    results = []

    positive_count = 0
    negative_count = 0
    neutral_count = 0

    positive_words = [
        "growth",
        "strong",
        "profit",
        "boost",
        "record",
        "demand",
        "expands",
        "rise",
        "gain"
    ]

    negative_words = [
        "risk",
        "fall",
        "warn",
        "slow",
        "tension",
        "concern",
        "decline",
        "drop",
        "loss"
    ]

    for headline in headlines:

        text = headline.lower()

        if any(word in text for word in positive_words):
            label = "positive"
            confidence = 0.70
            positive_count += 1

        elif any(word in text for word in negative_words):
            label = "negative"
            confidence = 0.70
            negative_count += 1

        else:
            label = "neutral"
            confidence = 0.60
            neutral_count += 1

        results.append({
            "headline": headline,
            "label": label,
            "confidence": confidence
        })

    if positive_count > negative_count:
        overall_sentiment = "Positive"

    elif negative_count > positive_count:
        overall_sentiment = "Negative"

    else:
        overall_sentiment = "Mixed / Neutral"

    summary = {
        "positive_count": positive_count,
        "negative_count": negative_count,
        "neutral_count": neutral_count,
        "overall_sentiment": overall_sentiment
    }

    return results, summary