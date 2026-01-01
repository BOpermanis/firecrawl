import pandas as pd
from io import StringIO
import numpy as np



def extract_tables(markdown_content):

    markdown_content = markdown_content.split("\n")

    inds = np.where([line.startswith("|") for line in markdown_content])[0]

    table_inds = []
    i1 = -100
    for i2 in range(len(inds)):
        if abs(inds[i1] - inds[i2]) > 1:
            table_inds.append([])
        table_inds[-1].append(inds[i2])
        i1 = i2


    dfs = []
    for inds in table_inds:
        markdown_table = "\n".join([markdown_content[i] for i in inds])
        df = pd.read_csv(StringIO(markdown_table), sep="|", skipinitialspace=True).dropna(axis=1, how='all').iloc[1:]
        dfs.append(df)

    return dfs

if __name__ == "__main__":
    from firecrawl import FirecrawlApp


    # No API key needed for self-hosted, but the SDK might whine if it's empty
    app = FirecrawlApp(api_url="http://localhost:3002", api_key="fc-YOUR_KEY")

    # Scrape the data and convert it to clean markdown, because HTML is gross
    response = app.scrape('https://invego.lv/vitolu/en/prices/all-apartments')
    print(11)
    with open("output.md", "w", encoding="utf-8") as f:
        f.write(response.markdown)


    with open("output.md", "r", encoding="utf-8") as f:
        markdown_content = f.read()

    tables = extract_tables(markdown_content)
    