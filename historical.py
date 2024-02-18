import pandas as pd
import matplotlib.pyplot as plt

import yfinance as yf

# Fetch historical price data for a stock or cryptocurrency
data = yf.download('BTC-USD', start='2023-10-01', end='2024-02-17')

# Calculate a 50-day Simple Moving Average (SMA)
data['SMA_50'] = data['Close'].rolling(window=50).mean()

# Plot the closing price and the SMA
plt.figure(figsize=(14, 7))
plt.plot(data['Close'], label='BTC-USD Close', alpha=0.5)
plt.plot(data['SMA_50'], label='50-Day SMA', alpha=0.75)
plt.title('BTC-USD Close Price and 50-Day SMA')
plt.legend()
plt.show()
