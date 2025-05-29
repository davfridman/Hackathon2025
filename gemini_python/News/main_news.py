from gemini import init_model
from news_fetcher import fetch_stock_news

# Step 1: Initialize Gemini model
gemini = init_model("gemini-1.5-flash")

# Step 2: Choose a stock keyword
keyword = "Nvidia"
articles = fetch_stock_news(keyword, max_articles=3)

# Step 3: Summarize each article title with Gemini
for article in articles:
    prompt = f"Given this news headline: \"{article['title']}\", what might be the potential market impact?"
    summary = gemini.ask(prompt, short_answer=True)

    print(f"📰 {article['title']}")
    print(f"🔗 {article['link']}")
    print(f"🧠 Summary: {summary}")
    print("-" * 80)