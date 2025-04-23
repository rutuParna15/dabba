# Install required libraries
# !pip install yfinance pandas numpy matplotlib statsmodels

# Import libraries
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error

# Step 1: Load time series data (Gold price example)
gold_data = yf.download('GC=F', start='2015-01-01', end='2023-12-31')
gold_prices = gold_data['Close'].dropna()
gold_prices = gold_prices.asfreq('D')  # Daily frequency

# Step 2: Plot the data
plt.figure(figsize=(10, 6))
plt.plot(gold_prices)
plt.title('Gold Price Over Time')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.show()

# Step 3: Check stationarity
result = adfuller(gold_prices.dropna())
print('ADF Statistic:', result[0])
print('p-value:', result[1])
if result[1] > 0.05:
    print("Data is non-stationary. Proceeding with differencing.")

# Step 4: Differencing
diff_data = gold_prices.diff().dropna()

plt.figure(figsize=(10, 6))
plt.plot(diff_data)
plt.title('Differenced Gold Prices')
plt.show()

# Step 5: ACF and PACF plots
plot_acf(diff_data.dropna(), lags=20)
plot_pacf(diff_data.dropna(), lags=20)
plt.show()

# Step 6: Fit ARIMA model
model = ARIMA(gold_prices, order=(1, 1, 1))  # ARIMA(p,d,q)
model_fit = model.fit()
print(model_fit.summary())

# Step 7: Forecast
forecast = model_fit.forecast(steps=30)
forecast_index = pd.date_range(start=gold_prices.index[-1], periods=31, freq='D')[1:]

plt.figure(figsize=(10, 6))
plt.plot(gold_prices, label='Historical')
plt.plot(forecast_index, forecast, label='Forecast', color='red')
plt.legend()
plt.title('Gold Price Forecast')
plt.show()
