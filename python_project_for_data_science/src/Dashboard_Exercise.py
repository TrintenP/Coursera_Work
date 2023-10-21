import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Define a graphing Function
def makeGraph(stockData:pd.DataFrame, revenueData:pd.DataFrame, stock:str):
    """
    stockData: pd.DataFrame, must have Date and Close columns
    revenueData: pd.DataFrame, must have Date and Revenue columns
    stock: str, name of the stock being graphed
    """

    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing= .3)
    stockDataSpecific = stockData[stockData.Date <= '2021--06-14']
    revenueDataSpecific = revenueData[revenueData.Date <= '2021-04-30']
    fig.add_trace(go.Scatter(x=pd.to_datetime(stockDataSpecific.Date, infer_datetime_format=True), y=stockDataSpecific.Close.asType("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenueDataSpecific.Date, infer_datetime_format=True), y=revenueDataSpecific.Close.asType("float"), name="Share Price"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False, height=900, title=stock, xaxis_rangeslider_visible=True)
    fig.show()

# Question 1: Use yfinance to extract stock data of Tesla (TLSA)
stockData = yf.Ticker('TSLA')

tesla_data = stockData.history(period='max')
tesla_data.reset_index(inplace=True)
# print(tesla_data.head())

# Question 2: Use Webscraping to extract tesla Revenue Data
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"

tesla_revenue = pd.read_html(url)[1]
tesla_revenue.columns = columns=["Date", "Revenue"]

# Remove symbols from Revenue colum (Data Cleaning)
tesla_revenue["Revenue"] = tesla_revenue["Revenue"].str.replace(",", "")
tesla_revenue["Revenue"] = tesla_revenue["Revenue"].str.replace("$", "")

# Remove Empty values
tesla_revenue.dropna(inplace=True)
tesla_revenue = tesla_revenue[tesla_revenue["Revenue"] != ""]

# Display last 5 rows
# print(tesla_revenue.tail())


# Question 3: Use yfinance to extract stock data
stockData = yf.Ticker("GME")
gme_date = stockData.history(period="max")
gme_date.reset_index(inplace=True)
print(gme_date.head())


# Question4: Use Webscraping to Extract GME Revenue Data