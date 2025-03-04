e Load Forecasting Project

This project aims to forecast the electrical/network load for each province one month (30 days) into the future. It is built using historical telecom data and follows best practices for data preprocessing, exploratory data analysis (EDA), and time series forecasting using Prophet.

## Table of Contents

- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Project Structure](#project-structure)
- [Installation and Setup](#installation-and-setup)
- [Usage](#usage)
  - [Data Preprocessing](#data-preprocessing)
    - [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
      - [Forecasting Model](#forecasting-model)
        - [Testing](#testing)
        - [Results](#results)
        - [Future Work](#future-work)
        - [License](#license)

        ## Project Overview

        The objective of this project is to analyze telecom load data per province and build forecasting models that predict load values for each province 30 days beyond the last recorded date. Each province is analyzed separately to capture unique trends and seasonality.

        ## Dataset

        The raw data file, `provinceDATA.csv`, is located in the `data/raw/` folder. It contains measurements with various features, but for this project, the key columns used are:

        - **PERIOD_START_TIME**: Date and time when the measurement was recorded.
        - **PROVINCE**: Province identifier.
        - **Load**: The load measurement to be forecasted.

        After preprocessing, the cleaned data is saved as `clean_provinceDATA.csv` in the `data/processed/` folder.

        ## Project Structure

        ```plaintext
        telecom-time-series/
        ├── data/
        │   ├── raw/
        │   │   └── provinceDATA.csv          # Raw data file
        │   ├── processed/
        │       ├── clean_provinceDATA.csv    # Cleaned data after preprocessing
        │       └── forecast_<PROVINCE>.csv    # Forecast results for each province (saved automatically)
        ├── docs/
        │   └── Data_Dictionary.md            # (Optional) Detailed description of dataset columns
        ├── notebooks/
        │   ├── EDA.ipynb                     # Notebook for exploratory data analysis (per-province)
        │   └── Forecast.ipynb                # Notebook for forecasting 30-day ahead load per province
        ├── scripts/
        │   ├── preprocess.py                 # Script to clean and preprocess the raw data
        │   └── train_forecast.py             # (Optional) Script version for forecasting
        ├── tests/
        │   └── test_forecast.py              # (Optional) Test cases for forecast outputs
        ├── README.md                         # This file
        └── .gitignore                        # Specifies files/folders to ignore (e.g., venv, __pycache__)
        Province Load Forecasting Project

This project aims to forecast the electrical/network load for each province one month (30 days) into the future. It is built using historical telecom data and follows best practices for data preprocessing, exploratory data analysis (EDA), and time series forecasting using Prophet.

## Table of Contents

- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Project Structure](#project-structure)
- [Installation and Setup](#installation-and-setup)
- [Usage](#usage)
  - [Data Preprocessing](#data-preprocessing)
  - [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
  - [Forecasting Model](#forecasting-model)
  - [Testing](#testing)
- [Results](#results)
- [Future Work](#future-work)
- [License](#license)

## Project Overview

The objective of this project is to analyze telecom load data per province and build forecasting models that predict load values for each province 30 days beyond the last recorded date. Each province is analyzed separately to capture unique trends and seasonality.

## Dataset

The raw data file, `provinceDATA.csv`, is located in the `data/raw/` folder. It contains measurements with various features, but for this project, the key columns used are:

- **PERIOD_START_TIME**: Date and time when the measurement was recorded.
- **PROVINCE**: Province identifier.
- **Load**: The load measurement to be forecasted.

After preprocessing, the cleaned data is saved as `clean_provinceDATA.csv` in the `data/processed/` folder.

## Project Structure

```plaintext
telecom-time-series/
├── data/
│   ├── raw/
│   │   └── provinceDATA.csv          # Raw data file
│   ├── processed/
│       ├── clean_provinceDATA.csv    # Cleaned data after preprocessing
│       └── forecast_<PROVINCE>.csv    # Forecast results for each province (saved automatically)
├── docs/
│   └── Data_Dictionary.md            # (Optional) Detailed description of dataset columns
├── notebooks/
│   ├── EDA.ipynb                     # Notebook for exploratory data analysis (per-province)
│   └── Forecast.ipynb                # Notebook for forecasting 30-day ahead load per province
├── scripts/
│   ├── preprocess.py                 # Script to clean and preprocess the raw data
│   └── train_forecast.py             # (Optional) Script version for forecasting
├── tests/
│   └── test_forecast.py              # (Optional) Test cases for forecast outputs
├── README.md                         # This file
└── .gitignore                        # Specifies files/folders to ignore (e.g., venv, __pycache__)

