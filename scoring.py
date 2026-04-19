def normalize(series):
    return (series - series.min()) / (series.max() - series.min())

def calculate_scores(df):
    if df.empty:
        return df

    # ✅ Safety check for missing columns
    required_cols = ["Returns", "VolumeSpike", "Trend"]
    for col in required_cols:
        if col not in df.columns:
            return df

    df = df.copy()

    df["ReturnsScore"] = normalize(df["Returns"])
    df["VolumeScore"] = normalize(df["VolumeSpike"])
    df["TrendScore"] = df["Trend"].astype(int)

    df["FinalScore"] = (
        df["ReturnsScore"] * 0.4 +
        df["VolumeScore"] * 0.4 +
        df["TrendScore"] * 0.2
    )

    return df.sort_values(by="FinalScore", ascending=False)
