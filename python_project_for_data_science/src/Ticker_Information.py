import yfinance as yf
import pandas as pd

apple = yf.Ticker("AAPL")

# Extract share price
apple_share_price_data = apple.history(period="max")

apple_share_price_data.reset_index(inplace=True)

# Plot opening prices versus date
# apple_share_price_data.plot(x='Date', y='Open')

# Plot dividends overtime
# apple.dividends.plot()
# plt.show()

# Exercise