import pandas as pd
import matplotlib.pyplot as plt
import pandas_ta as ta
import yfinance as yf

# Fetch historical price data
data = yf.download('BTC-USD', start='2023-01-01', end='2023-12-31')

# Calculate SMA (50 days)
data['SMA_50'] = ta.sma(data['Close'], length=50)

# Calculate RSI (14 days)
data['RSI_14'] = ta.rsi(data['Close'], length=14)


# # Assuming `data` is your DataFrame and it already contains 'Close' column
# bbands = ta.bbands(data['Close'], length=20, std=2)
#
# # Ensure the column names match the ones in the returned DataFrame from ta.bbands()
# data[['Bollinger_Upper', 'Bollinger_Middle', 'Bollinger_Lower']] = bbands

# Plotting
plt.figure(figsize=(14, 10))

# Plot Close Price and SMA
plt.subplot(311)
plt.plot(data['Close'], label='Close Price', alpha=0.5)
plt.plot(data['SMA_50'], label='50-Day SMA', alpha=0.75)
plt.title('Close Price and 50-Day SMA')
plt.legend()

# Plot RSI
plt.subplot(312)
plt.plot(data['RSI_14'], label='14-Day RSI', color='purple')
plt.title('Relative Strength Index (14-Day)')
plt.axhline(70, linestyle='--', alpha=0.5, color='red')
plt.axhline(30, linestyle='--', alpha=0.5, color='green')

# # Plot Bollinger Bands
# plt.subplot(313)
# plt.plot(data['Close'], label='Close Price', alpha=0.5)
# plt.plot(data['Bollinger_Upper'], label='Upper Band', alpha=0.75, linestyle='--', color='red')
# plt.plot(data['Bollinger_Middle'], label='Middle Band', alpha=0.75, color='blue')
# plt.plot(data['Bollinger_Lower'], label='Lower Band', alpha=0.75, linestyle='--', color='green')
# plt.title('Bollinger Bands')

plt.legend()
plt.tight_layout()
plt.show()
