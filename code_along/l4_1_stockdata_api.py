"""
Introduktion av plocka data från ett API
I detta fall aktier från Avanza
# alphavantage.com
path = r"https://www.alphavantage.co/"

pipenv install python-dotenv
pipenv install requests
"""
import requests
from dotenv import load_dotenv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import time

"""load_dotenv()
api_key= os.getenv("ALPHA_API_KEY")
symbol = "AAPL"
#print(api_key)"""


"""
url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize=full&apikey={api_key}"
data = requests.get(url).json()
df = pd.DataFrame(data['Time Series (Daily)']).transpose().astype(float) # eller .T
df.head()
df.info()
df.index

df.index= pd.to_datetime(df.index)
df.loc["2021-10-20": "2021-10-29"]  # [start+1 : stop ]
"""

"""
symbols = ["APPL", "TSLA", "NVDA", "IBM"]
stock_list = []

for symbol in symbols:
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize=full&apikey={api_key}"
    data = requests.get(url).json()
    df = pd.DataFrame(data['Time Series (Daily)']).transpose()
    df = df["4. close"].rename(symbol).astype(float)
    stock_list.append(df)
    time.sleep(20)

stocks = pd.concat(stock_list, axis=1)
stocks.to_csv("stocks.csv", sep=",")
"""

stocks = pd.read_csv("stocks.csv")
stocks.head()
stocks.info()

# subplots
fig, ax = plt.subplots(2,2, dpi=100, figsize=(12,6))
#print(ax.shape)             # ger (2,2)
#print(ax.flatten().shape)  # ger (4,)

stock_2021 = stocks.loc["2021"]
stock_names = dict(APPL ="Apple", NVDA= "Nvidia", TSLA="Tesla", IBM = "IBM")

for ax, symbol in zip(ax.flatten(), stock_names):
    print(symbol)
    sns.lineplot(data=stock_2021, x=stock_2021.index, y=symbol, ax=ax)
    ax.tick_params(axis="x", rotation=45)
    ax.set(title=f"{stock_names[symbol]}", ylabel="Price in dollars")

fig.thight_layout()
fig.suptitle("Stocks during 2021", y=1.03, fontweight="bold")


   




