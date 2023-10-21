import pandas as pd
import requests
from bs4 import BeautifulSoup


url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/amazon_data_webpage.html"
html_data = requests.get(url).text

soup = BeautifulSoup(html_data, "html5lib")

# Question 1: What is the content of the title attribute?
# Answer 1: Amazon.com, Inc. (AMZN) Stock Historical Prices & Data - Yahoo Finance
print(soup.title.text)

amazonData = pd.DataFrame(columns=['Date', "Open", "High", "Low", "Close", "Volume"])

tagList = soup.find('tbody').find_all(name='tr')

for row in tagList:
    col = row.find_all(name="td")

    date = col[0].text
    openPrice = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    volume = col[6].text
        
    amazonData = amazonData._append({'Date':date,'Open':openPrice,'High':high,"Low":low,"Close":close,"Volume":volume}, ignore_index=True)

# Print out first five rows created
print(amazonData.head())

# Question 2: What are the names of the columns in the data frame?
# Answer 2: Date Open High Low Close Volume
print(amazonData.columns)

# Question 3: What is the Open of the last row of the data frame?
# Answer 3: 656.29
print(amazonData['Open'].iloc[-1])