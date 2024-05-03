import pandas as pd
import numpy as np
import random
# read from finvizurls.txt
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import Request
from datetime import date
from nltk.sentiment.vader import SentimentIntensityAnalyzer

vader = SentimentIntensityAnalyzer()

class HistoricalSentiment:

    def __init__(self, ticker, fn=vader.polarity_scores):
        self.ticker = ticker
        self.fn = fn

    def find_articles(self):
        url_req = f"{url}/quote.ashx?t={self.ticker}"
        req = Request(url=url_req, headers={"User-Agent": "FireFox"}) # I realize that aditya's version of the code doesn't use the right user agent
        response = urlopen(req)
        html = BeautifulSoup(response, "html.parser")
        news_table = html.find(id='news-table')

        return news_table
    
    def generate_news_df(self, news_table):
        news_list = []
        # oldest.datetime_timestamp
        # datetime.datetime(1998, 11, 11, 18, 45, 51)

        # TODO: filter based on time (i.e. use previous day to get news for next day)

        for i in news_table.findAll('tr'):
            try:
                text = i.a.get_text()
            except:
                continue

            date_scrape = i.td.text.split()
            source = i.div.span.get_text()

            if len(date_scrape) == 1:
                time = date_scrape[0]

            else:
                final_date = date_scrape[0]
                time = date_scrape[1]

                if final_date == "Today":
                    final_date = date.today().strftime("%Y-%m-%d")

            tick = self.ticker

            news_list.append([tick, final_date, time, source, text])

        columns = ['ticker', 'date', 'time', 'source', 'headline']
        news_df = pd.DataFrame(news_list, columns=columns)
        news_df['date'] = pd.to_datetime(news_df.date, format='mixed').dt.date

        # randomly select 40 headlines from 40 different days. This will have to be stratified by date
        for i in range(40):
            news_df = news_df.sample(frac=1).groupby('date').head(1)

        return news_df
    
    def calculate_sentiment(self):
        self.news_scraped = self.find_articles()
        self.news_df = self.generate_news_df(self.news_scraped)
        # requires that find_articles has been called and generated a news_df

        scores = self.news_df['headline'].apply(self.fn).tolist()
        scores = [x['compound'] for x in scores]
        sentiment = float(np.mean(scores))
        final_sentiment = round(sentiment, 4)
        print(self.news_df.head())
        return self.news_df['headline'], final_sentiment
    
# def get_urls():
with open("finvizurls.txt", "r") as f:
    urls = f.readlines()

random.seed(0)
# format of each url is https://web.archive.org/web/20210102072011/https://www.finviz.com/
# need to get the timestamp from each url. Make sure the timestamp is the market close of each day
# 20210102072011 -> 2021-01-02 07:20:11 UTC

urls_select = random.sample(range(len(urls)), 40)
urls_select = [urls[i] for i in urls_select]
news_tables = {}

tickers = ["MSFT"]

print("urls selected", urls_select)

for url in urls_select:
    # save url to access metadata
    # beatiful soup to extract the text
    url = url.strip()
    for ticker in tickers:
        headline, sentiment = HistoricalSentiment(ticker).calculate_sentiment()
        print("headline", headline)
        print("sentiment", sentiment)
        break


# ticker                                                   MSFT
# date                                               2020-12-31
# time                                                  05:03PM
# source                                            Barrons.com
# headline    Section 230 Keeps Coming Up in Congress. Heres...
# news_list = []


# #TODO: compare vader polarity vs our version

# def get_scores(df):
#     scores = df['headline'].apply(vader.polarity_scores).tolist()
#     scores = [x['compound'] for x in scores]
#     sentiment = float(np.mean(scores))
#     final_sentiment = round(sentiment, 4)
#     return final_sentiment

# # print("vader", get_scores(news_df))