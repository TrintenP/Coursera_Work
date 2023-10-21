import yfinance as yf
import pandas as pd

# Use the Ticker Module to create and object for AMD; call the object amd
amd = yf.Ticker("AMD")

# Using the key 'country' what country does the stock belong to?
print(amd.info['country'])

# Using the key 'sector' what sector does the stock belong to?
print(amd.info['sector'])

# Obtain stock data for AMD; set the period to max; Find the volumne traded on the first day
print(amd.history(period='max')['Volume'].iloc[0])