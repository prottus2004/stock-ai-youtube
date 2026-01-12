import feedparser
from datetime import datetime, timedelta

FEEDS = [
    "https://news.google.com/rss/search?q=US+stock+market+NASDAQ+SP500",
    "https://finance.yahoo.com/news/rssindex"
]

def fetch_news():
    results = []
    now = datetime.utcnow()

    for url in FEEDS:
        feed = feedparser.parse(url)
        for e in feed.entries:
            if hasattr(e, "published_parsed"):
                published = datetime(*e.published_parsed[:6])
                if now - published < timedelta(hours=6):
                    results.append({
                        "title": e.title,
                        "summary": e.get("summary", ""),
                        "link": e.link
                    })
    return results

