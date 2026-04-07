{\rtf1\ansi\ansicpg1252\cocoartf2868
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import yfinance as yf\
import pandas as pd\
\
STOCKS = [\
    "RELIANCE.NS", "TCS.NS", "INFY.NS", "HDFCBANK.NS",\
    "ICICIBANK.NS", "SBIN.NS", "LT.NS", "ITC.NS",\
    "AXISBANK.NS", "KOTAKBANK.NS"\
]\
\
def fetch_data():\
    data = []\
\
    for stock in STOCKS:\
        try:\
            df = yf.download(stock, period="3mo", interval="1d", progress=False)\
\
            if df.empty:\
                continue\
\
            df["Returns"] = df["Close"].pct_change(7)\
            df["AvgVolume"] = df["Volume"].rolling(20).mean()\
            df["VolumeSpike"] = df["Volume"] / df["AvgVolume"]\
            df["MA20"] = df["Close"].rolling(20).mean()\
\
            latest = df.iloc[-1]\
\
            data.append(\{\
                "Ticker": stock,\
                "Price": latest["Close"],\
                "Returns": latest["Returns"],\
                "VolumeSpike": latest["VolumeSpike"],\
                "Trend": latest["Close"] > latest["MA20"]\
            \})\
\
        except Exception as e:\
            print(f"Error: \{e\}")\
\
    return pd.DataFrame(data)}