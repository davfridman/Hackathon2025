import feedparser

def fetch_stock_news(keyword, max_articles=5):
    """
    Fetch recent news headlines for a company/keyword from Google News RSS.
    
    Args:
        keyword (str): e.g., 'Nvidia' or 'AAPL'
        max_articles (int): Max number of headlines to return
        
    Returns:
        List[dict]: List of news articles with title, link, and date
    """
    url = f"https://news.google.com/rss/search?q={keyword}+stock"
    feed = feedparser.parse(url)

    articles = []
    for entry in feed.entries[:max_articles]:
        articles.append({
            "title": entry.title,
            "link": entry.link,
            "published": entry.published
        })

    return articles
