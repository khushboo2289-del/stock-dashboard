{\rtf1\ansi\ansicpg1252\cocoartf2868
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 def normalize(series):\
    return (series - series.min()) / (series.max() - series.min())\
\
def calculate_scores(df):\
    df = df.copy()\
\
    df["ReturnsScore"] = normalize(df["Returns"])\
    df["VolumeScore"] = normalize(df["VolumeSpike"])\
    df["TrendScore"] = df["Trend"].astype(int)\
\
    df["FinalScore"] = (\
        df["ReturnsScore"] * 0.4 +\
        df["VolumeScore"] * 0.4 +\
        df["TrendScore"] * 0.2\
    )\
\
    return df.sort_values(by="FinalScore", ascending=False)}