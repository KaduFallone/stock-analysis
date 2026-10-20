import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import yfinance as yf
import mplcyberpunk as mcp

#Select the bank stocks and the Bovespa index
ticker_list = ["BBAS3.SA","SANB4.SA","ITUB4.SA","BBDC4.SA","^BVSP"]
bank_data = yf.download(ticker_list, start="2009-12-31", end="2021-12-31")

#Keep only the closing prices
bank_data = bank_data["Close"]

#Load the banks' profit data
bank_profits = pd.read_excel("lucros_bancos.xlsx")

#Split the data for each bank and the Bovespa index
bank_of_brazil = bank_data["BBAS3.SA"]
santander = bank_data["SANB4.SA"]
itau = bank_data["ITUB4.SA"]
bradesco = bank_data["BBDC4.SA"]
market_data = bank_data["^BVSP"]

#Calculate stock returns (final price / initial price - 1)
def calculate_return(price_list):
    stock_return = price_list.iloc[-1] / price_list.iloc[0] - 1

    return stock_return

#Calculate the return of each asset separately
bb_return = calculate_return(bank_of_brazil)
santander_return = calculate_return(santander)
itau_return = calculate_return(itau)
bradesco_return = calculate_return(bradesco)
market_return = calculate_return(market_data)

#Create a dataframe to store the returns
df_returns = pd.DataFrame(
    data = {"return": [bb_return,santander_return,itau_return,bradesco_return,market_return]},
    index = ["Banco do Brasil", "Santander", "Itau","Bradesco","Ibovespa"]
)

#Convert the returns to percentages and sort them in descending order
df_returns = df_returns * 100
df_returns = df_returns.sort_values(by = "return", ascending  = False)

#Create a simple bar chart of the returns
plt.style.use("cyberpunk")
fig, ax = plt.subplots()
ax.bar(x = df_returns.index, height = df_returns["return"])
ax.yaxis.set_major_formatter(mtick.PercentFormatter())
plt.xticks(fontsize = 9)
plt.show()
