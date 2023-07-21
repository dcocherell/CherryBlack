from chryblk.models import QuandlData
import requests
import pandas as pd
from datetime import datetime

def update_stocks():
    api_key = "ys9S8-5W3HoXrwH92MWK"
    companies = ["FB", "AAPL", "MSFT", "GOOGL", "TSLA", "JNJ", "JPM", "NVDA", "WMT", "NFLX"]
    data_list = []

    for company in companies:
        url = f"https://data.nasdaq.com/api/v3/datasets/WIKI/{company}.json?api_key={api_key}"
        response = requests.get(url)
        data = response.json()

        most_recent_data = data['dataset']['data'][0]
        previous_day_data = data['dataset']['data'][1]

        change = (most_recent_data[4] - previous_day_data[4]) / previous_day_data[4] * 100

        data_list.append({
            "ticker": company,
            "date": datetime.strptime(most_recent_data[0], '%Y-%m-%d').date(),
            "open_price": most_recent_data[1],
            "high": most_recent_data[2],
            "low": most_recent_data[3],
            "close": most_recent_data[4],
            "volume": most_recent_data[5],
            "change": change,
        })

    df = pd.DataFrame(data_list)
    df = df.sort_values("change", ascending=False)
    print(df)

    QuandlData.objects.all().delete()

    for row in df.itertuples():
        QuandlData.objects.create(
            ticker=getattr(row, 'ticker'),
            date=getattr(row, 'date'),
            open_price=getattr(row, 'open_price'),
            high=getattr(row, 'high'),
            low=getattr(row, 'low'),
            close=getattr(row, 'close'),
            volume=getattr(row, 'volume'),
            change=getattr(row, 'change'),
        )