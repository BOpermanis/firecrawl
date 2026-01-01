from firecrawl import FirecrawlApp


# No API key needed for self-hosted, but the SDK might whine if it's empty
app = FirecrawlApp(api_url="http://localhost:3002", api_key="fc-YOUR_KEY")

# Scrape the data and convert it to clean markdown, because HTML is gross
response = app.scrape('https://invego.lv/vitolu/en/prices/all-apartments')
print(11)
with open("output.md", "w", encoding="utf-8") as f:
    f.write(response.markdown)


