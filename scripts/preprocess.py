import os
<<<<<<< HEAD
import pandas as pd
=======
os.getcwd()
print("Current working directory:", os.getcwd())
# Using relative paths from the project root
data_file = os.path.join("data", "raw", "teleco_time_series.csv")
>>>>>>> e2645ed4b77c08d555bc38fd7af5fe70cbc8f030

# Build a robust relative path from this script's location
script_dir = os.path.dirname(os.path.abspath(__file__))
raw_data_path = os.path.join(script_dir, '..', 'data', 'raw', 'provinceDATA.csv')
processed_data_path = os.path.join(script_dir, '..', 'data', 'processed', 'clean_provinceDATA.csv')

#print("Raw data file path:", raw_data_path)

# Load raw data (make sure the 'date' column is parsed as datetime)
df = pd.read_csv(raw_data_path, parse_dates=['PERIOD_START_TIME'])
print("Raw data shape:", df.shape)
# Initial Cleaning Steps:
# 1. Check for missing values and fill or drop as necessary
#print("Missing values before cleaning:", df.isnull().sum())

#print("Raw data summary:")
#print(df.describe())

import seaborn as sns
import matplotlib.pyplot as plt

#plt.figure(figsize=(12, 4))
#sns.heatmap(df.isnull(), cbar=False)
#plt.title("Missing Data in Raw Data")
#plt.show()
missing_percent = df.isnull().mean() * 100
# Drop columns with more than 80% missing data
threshold = 80
cols_to_drop = missing_percent[missing_percent > threshold].index
df_reduced = df.drop(columns=cols_to_drop)
print("Columns dropped:", list(cols_to_drop))
df = df.drop(columns=cols_to_drop)
df.fillna(method='ffill')
#df = df.dropna() 

 
# 2. Ensure data types are correct (e.g., 'province' as string, 'load' as float)
df['PROVINCE'] = df['PROVINCE'].astype(str)
df['Load'] = pd.to_numeric(df['Load'], errors='coerce')
df = df.dropna(subset=['Load'])  # Drop rows where 'load' conversion failed

# (Optional) Pivot the data if you want a wide format per date:
df_pivot = df.pivot(index='date', columns='province', values='load')

# Save the cleaned data for further analysis
df.to_csv(processed_data_path, index=False)
print("Data preprocessing complete. Clean data saved at:", processed_data_path)

#print("Missing values in clean data:")
#print(df.isnull().sum())
#print("Clean data summary:")
#print(df.describe())
print("clean data shape:", df.shape)