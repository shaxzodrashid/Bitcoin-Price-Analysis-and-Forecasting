# Importing necessary libraries
import requests
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
import warnings

# Disabling ARIMA model warnings
warnings.filterwarnings("ignore")

# 1st step: Fetching data
# Function to fetch Bitcoin prices using CoinGecko API

def fetch_bitcoin_data(days=30):
    """
    Fetches the last 'days' days of Bitcoin prices from CoinGecko API.
    """
    url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
    params = {'vs_currency': 'usd', 'days': days}
    response = requests.get(url, params=params)
    data = response.json()
    # Converting prices to DataFrame
    prices = pd.DataFrame(data['prices'], columns=['timestamp', 'price'])
    prices['date'] = pd.to_datetime(prices['timestamp'], unit='ms')
    # Setting 'date' column as index
    prices.set_index('date', inplace=True)
    # Dropping 'timestamp' column
    prices.drop('timestamp', axis=1, inplace=True)
    return prices

# Fetching data
prices = fetch_bitcoin_data(60)  # Fetching the last 60 days of data

# 2nd step: Data preprocessing

# Checking for missing values
print("Missing values in the data:")
print(prices.isnull().sum())

# Calculating percentage change in prices
prices['price_change_pct'] = prices['price'].pct_change() * 100

# Dropping NaN values
prices.dropna(inplace=True)

# 3rd step: Data analysis

# Statistical analysis
mean_price = prices['price'].mean()
median_price = prices['price'].median()
max_price = prices['price'].max()
min_price = prices['price'].min()

print(f"Average price: ${mean_price:.2f}")
print(f"Median price: ${median_price:.2f}")
print(f"Maximum price: ${max_price:.2f}")
print(f"Minimum price: ${min_price:.2f}")

# 4th step: Visualization

# Plotting prices over time
plt.figure(figsize=(12,6))
plt.plot(prices.index, prices['price'], label='Bitcoin Price')
plt.title('Bitcoin Price Over Time')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.show()

# Plotting daily percentage change
plt.figure(figsize=(12,6))
plt.plot(prices.index, prices['price_change_pct'], label='Daily Percentage Change')
plt.title('Bitcoin Daily Percentage Change')
plt.xlabel('Date')
plt.ylabel('Percentage Change (%)')
plt.legend()
plt.show()

# 5th step: Forecasting using ARIMA model

# Function to check stationarity using Augmented Dickey-Fuller test
from statsmodels.tsa.stattools import adfuller

def test_stationarity(timeseries):
    # Running ADF test
    result = adfuller(timeseries)
    print('ADF Statistic:', result[0])
    print('p-value:', result[1])
    if result[1] <= 0.05:
        print("The time series is stationary.")
    else:
        print("The time series is not stationary.")

# Checking stationarity
test_stationarity(prices['price'])

# Achieving stationarity by differencing
prices['price_diff'] = prices['price'].diff()
prices.dropna(inplace=True)

# Checking stationarity again
print("\nAfter differencing:")
test_stationarity(prices['price_diff'])

# Building ARIMA model
model = ARIMA(prices['price'], order=(5,1,0))  # Tuning (p,d,q) parameters is possible
model_fit = model.fit()

# Forecasting the next 10 days
forecast_steps = 10
forecast = model_fit.forecast(steps=forecast_steps)

# Creating date range for forecast
last_date = prices.index[-1]
forecast_dates = pd.date_range(last_date, periods=forecast_steps+1, freq='D')[1:]

# Plotting forecasted prices
plt.figure(figsize=(12,6))
plt.plot(prices.index, prices['price'], label='Historical Price')
plt.plot(forecast_dates, forecast, label='Forecasted Price', color='red')
plt.title('Bitcoin Price Forecast')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.show()

# Printing forecasted prices
forecast_df = pd.DataFrame({'Date': forecast_dates, 'Forecasted Price': forecast.values})
print("\nForecasted Prices:")
print(forecast_df)