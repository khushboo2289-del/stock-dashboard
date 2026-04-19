import yfinance as yf
import pandas as pd

STOCKS = [
    "RELIANCE.NS", "TCS.NS", "INFY.NS", "HDFCBANK.NS",
    "ICICIBANK.NS", "SBIN.NS", "LT.NS", "ITC.NS",
    "AXISBANK.NS", "KOTAKBANK.NS"
]

def fetch_data():
    data = []

    for stock in STOCKS:
        df = yf.download(stock, period="3mo", interval="1d", progress=False)

        if df.empty:
            continue

        df["Returns"] = df["Close"].pct_change(7)
        df["AvgVolume"] = df["Volume"].rolling(20).mean()
        df["VolumeSpike"] = df["Volume"] / df["AvgVolume"]
        df["VolumeSpike"] = df["VolumeSpike"].fillna(0)
        df["MA20"] = df["Close"].rolling(20).mean()

        df = df.dropna()

        latest = df.iloc[-1]

        data.append({
            "Ticker": stock,
            "Price": latest["Close"],
            "Returns": latest["Returns"],
            "VolumeSpike": latest["VolumeSpike"],
            "Trend": latest["Close"] > latest["MA20"]
        })

    return pd.DataFrame(data)
