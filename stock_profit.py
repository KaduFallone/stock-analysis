import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import yfinance as yf
import mplcyberpunk as mcp
plt.style.use("cyberpunk")

#Load the banks' profit data
bank_profits = pd.read_excel("lucros_bancos.xlsx")


#Compare the change in the banks' profits (lucros_bancos.xlsx)
bank_profits = bank_profits.set_index("data")
profit_change = bank_profits.iloc[-1]/bank_profits.iloc[0] -1
profit_change = profit_change * 100
profit_change = profit_change.sort_values(ascending = False)

#Create a simple bar chart of the change in the banks' profits
fig, ax = plt.subplots()
ax.bar(x = profit_change.index, height = profit_change.values)
ax.yaxis.set_major_formatter(mtick.PercentFormatter())
plt.xticks(fontsize = 9)
plt.show()
