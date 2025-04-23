# !pip install yfinance statsmodels matplotlib pandas

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# Step 1: Download historical gold prices (using GLD ETF as a proxy)
gold_data = yf.download('GLD', start='2015-01-01', end='2024-12-31')

# Step 2: Check available columns
print("Available columns:", gold_data.columns)

# Use 'Close' column instead of 'Adj Close' if 'Adj Close' is not found
if 'Adj Close' in gold_data.columns:
    gold_prices = gold_data['Adj Close']
else:
    gold_prices = gold_data['Close']

# Set frequency to business days and fill missing values
gold_prices = gold_prices.asfreq('B').fillna(method='ffill')

# Step 3: Fit ARIMA model
model = ARIMA(gold_prices, order=(5,1,0))  # you can tune (p,d,q)
model_fit = model.fit()

# Step 4: Forecast future prices
forecast_steps = 30
forecast = model_fit.forecast(steps=forecast_steps)

# Step 5: Plot the results
plt.figure(figsize=(12, 6))
plt.plot(gold_prices, label='Historical Prices')
plt.plot(pd.date_range(gold_prices.index[-1], periods=forecast_steps+1, freq='B')[1:], forecast, label='Forecast', color='red')
plt.title('Gold Price Forecast (ARIMA)')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
