import feedparser


def get_recent_news(ticker, limit=5):

    rss_url = f"https://news.google.com/rss/search?q={ticker}+stock"

    feed = feedparser.parse(rss_url)

    headlines = []

    for entry in feed.entries[:limit]:
        headlines.append(entry.title)

    return headlines