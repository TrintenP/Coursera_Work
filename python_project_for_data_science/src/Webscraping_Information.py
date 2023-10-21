import pandas as pd
import requests
from bs4 import BeautifulSoup

# For this Information portion we will be extracting Netflix stock data from a webpage

netflixURL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html"

# This page has columns with the following names: Date, Open, High, Low, Close, Adj Close, Volume

# We must extract the following: Date, Open, High, Low, Close, Volume


# Steps for extracting the Data
# 1.) Send an HTTP request using requests library
# 2.) Parse the HTML content using BeautifulSoup library
# 3.) Identify HTML tags that contain the data we want to process
# 4.) Use BeautifulSoup to extract data from HTML tags
# 5.) print the extracted data

# Step 1
data = requests.get(netflixURL).text

# Step 2
soup = BeautifulSoup(data, 'html5lib')

# Step 3
netflixData = pd.DataFrame(columns=['Date', "Open", "High", "Low", "Close", "Volume"])

# Step 4
tagList = soup.tbody.find_all(name='tr')

for row in tagList:
    col = row.find_all(name="td")

    date = col[0].text
    openPrice = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    volume = col[6].text
        
    netflixData = netflixData._append({'Date':date,'Open':openPrice,'High':high,"Low":low,"Close":close,"Volume":volume}, ignore_index=True)

# Step 5
print(netflixData)


# Faster method
readHTMLData = pd.read_html(netflixURL)

# pd.read_html(str(soup))

# Since there is only one table on the page then read the first table
netflixDataFrame = readHTMLData[0]
print(netflixDataFrame.head())