# Bitcoin-Price-Analysis-and-Forecasting
A Python project that analyzes and forecasts Bitcoin prices using data from the CoinGecko API. The project performs statistical analysis, visualizations, and time series forecasting using the ARIMA model. This project demonstrates skills in data preprocessing, trend analysis, and predictive modeling.
# Bitcoin Price Analysis and Forecasting

This Python project analyzes historical Bitcoin prices and forecasts future prices using data from the CoinGecko API. The project covers data fetching, preprocessing, statistical analysis, visualizations, and predictive modeling using the ARIMA time series model.

## Features
- Fetch Bitcoin price data from CoinGecko API (up to 60 days).
- Perform statistical analysis (mean, median, max, min) of Bitcoin prices.
- Visualize price trends and daily percentage changes.
- Forecast Bitcoin prices for the next 10 days using the ARIMA model.
- Output forecasted price trends in a clean and user-friendly format.

## Project Structure
The project follows these main steps:
1. **Data fetching**: Bitcoin prices are fetched from CoinGecko API.
2. **Data preprocessing**: The dataset is cleaned, and percentage changes in prices are calculated.
3. **Statistical analysis**: Key statistics such as mean, median, max, and min prices are computed.
4. **Visualization**: Prices and daily percentage changes are visualized using Matplotlib.
5. **Forecasting**: Future prices are predicted using the ARIMA time series model.

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/bitcoin-price-analysis.git
```
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```
Usage
After setting up the environment and installing the dependencies, run the script to fetch, analyze, and visualize Bitcoin prices, as well as forecast the next 10 days of prices.
```bash
python bitcoin_analysis.py
```
## Dependencies
# requests
# pandas
# matplotlib
# statsmodels
You can install these dependencies using:
```bash
pip install requests pandas matplotlib statsmodels
```
