from celery import shared_task, Celery, signals
from .models import QuandlData
import yfinance as yf
from datetime import datetime
import time

@shared_task
def update_stocks():
    tickers = ['AAPL', 'MSFT', 'GOOGL', 'TSLA', 'BOH', 'JNJ', 'JPM', 'WMT', 'NVDA', 'NFLX']
    buy_threshold = -2
    sell_threshold = 2

    for ticker in tickers:
        print(f'Fetching data for {ticker}')
        try:
            stock = yf.Ticker(ticker)
            data = stock.history(period="2d")  # fetch data for the last 2 days
        except Exception as e:
            print(f"Error occurred while fetching data for {ticker}: {e}")
            continue

        if data.empty:
            print(f"No data available for {ticker}")
            continue

        most_recent_data = data.iloc[0]  # data for the most recent day
        previous_day_data = data.iloc[1]  # data for the day before

        change = (most_recent_data['Close'] - previous_day_data['Close']) / previous_day_data['Close'] * 100
        if change <= buy_threshold:
            recommendation = 'Buy'
        elif change >= sell_threshold:
            recommendation = 'Sell'
        else:
            recommendation = 'Hold'

        print(f"Saving data for {ticker}:")
        print(f"Date: {most_recent_data.name.date()}")
        print(f"Open: {most_recent_data['Open']}")
        print(f"High: {most_recent_data['High']}")
        print(f"Low: {most_recent_data['Low']}")
        print(f"Close: {most_recent_data['Close']}")
        print(f"Volume: {most_recent_data['Volume']}")
        print(f"Change: {change}")
        print(f"Average: {(most_recent_data['High'] + most_recent_data['Low']) / 2}")
        print(f"Recommendation: {recommendation}")

        QuandlData.objects.filter(ticker=ticker, date=most_recent_data.name.date()).delete()

        QuandlData.objects.create(
            ticker=ticker,
            date=most_recent_data.name.date(),
            open_price=most_recent_data['Open'],
            high=most_recent_data['High'],
            low=most_recent_data['Low'],
            close=most_recent_data['Close'],
            volume=int(most_recent_data['Volume']),
            change=change,
            average=(most_recent_data['High'] + most_recent_data['Low']) / 2,
            recommendation = recommendation
        )

        time.sleep(10)  # avoid hitting API limit

from prometheus_client import Counter

app = Celery('chryblk')

TASKS_SUCCESS = Counter('tasks_success_total', 'Tasks success')
TASKS_FAILURE = Counter('tasks_failure_total', 'Tasks failure')

@app.task
def add(x, y):
    return x + y

@app.task(bind=True)
def on_success(self, retval, task_id, args, kwargs):
    TASKS_SUCCESS.inc()

@app.task(bind=True)
def on_failure(self, exc, task_id, args, kwargs, einfo):
    TASKS_FAILURE.inc()
