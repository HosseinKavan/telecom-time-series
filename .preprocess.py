# scripts/preprocess.py
import pandas as pd

def load_data(filepath):
    return pd.read_csv(filepath)

def clean_data(df):
    # Example: Drop missing values and reset index
    df = df.dropna().reset_index(drop=True)
    return df

if __name__ == "__main__":
    # Load raw data
    df = load_data("data/raw/teleco_time_series.csv")
    # Clean data
    df_clean = clean_data(df)
    # Save cleaned data to processed folder
    df_clean.to_csv("data/processed/clean_time_series.csv", index=False)
    print("Data preprocessing complete.")
