import requests

from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
TWILIO_ACCOUNT_SID = "AC5679d5cfb0102a6a6a94bf1d6d573e0f"

STOCK_API_KEY = "ILOG6FYH4XQA7IS0"
NEWS_API_KEY = "67cf36c18f0a479491c9976995ef1460"
TWILIO_AUTH_TOKEN = "0b9e8cfc626c696e97b104888bc5c5b2"

stock_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}


def send_sms(headline: str):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    if is_increase:
        sign = "🔺"
    else:
        sign = "🔻"
    message = f"{STOCK_NAME}:  {sign} {round(percent_diff, 1)}% \n Headline: {headline}"
    client.messages.create(body=message, from_='+18556439996', to='+12093051453')


def good_news():
    news_params = {
        "q": COMPANY_NAME,
        "sortBy": "popularity",
        "apiKey": NEWS_API_KEY
    }
    news_json = requests.get(NEWS_ENDPOINT, params=news_params).json()
    top_news = news_json["articles"][0:3]
    headlines = [v["title"] for v in top_news]
    for headline in headlines:
        send_sms(headline)


resp = requests.get(STOCK_ENDPOINT, params=stock_params)
daily_data = resp.json()["Time Series (Daily)"]
data_list = [v for (k, v) in daily_data.items()]
yesterday_closing_price = float(data_list[0]["4. close"])
day_before_yesterday_closing_price = float(data_list[1]["4. close"])
is_increase = yesterday_closing_price > day_before_yesterday_closing_price
abs_diff = round(abs(day_before_yesterday_closing_price - yesterday_closing_price), 1)

percent_diff = (abs_diff / yesterday_closing_price) * 100
if percent_diff > .9:
    good_news()
