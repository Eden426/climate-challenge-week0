import pandas as pd

def load_data():
    # Use lower-case folder name 'data'; adjust if your path differs
    df = pd.read_csv("data/combined_clean.csv")

    df["DATE"] = pd.to_datetime(df["DATE"])
    df["Year"] = df["DATE"].dt.year
    df["Month"] = df["DATE"].dt.month

    return df