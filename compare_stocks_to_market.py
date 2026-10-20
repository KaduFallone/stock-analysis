import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import yfinance as yf
import mplcyberpunk as mcp
plt.style.use("cyberpunk")

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


#Resample the data to an annual period
def resample_period(data, period):
    resampled_data = data.resample(f"{period}").last()
    resampled_data = resampled_data.pct_change()
    resampled_data = resampled_data.dropna()

    return resampled_data


#Calculate the years in which the asset's price outperformed the market
def longShort_market(asset_data, period, asset_name):
    long = resample_period(asset_data, period)
    short = resample_period(market_data, period)
    long, short = long.align(short, join="inner")
    outperform = (long - short) * 100

    print(outperform)

    plt.figure(figsize=(10,5))
    plt.plot(outperform.index, outperform.values, marker="o")
    plt.title(f"Long x Short - Comparação: {asset_name} / Mercado")
    plt.ylabel("Diferença (%)")
    plt.grid(True)
    plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter())
    plt.show()



#Annual Long/Short analysis for each bank
longShort_market(bank_of_brazil, "YE", "BB")
longShort_market(santander, "YE", "Santander")
longShort_market(itau, "YE", "Itau")
longShort_market(bradesco, "YE", "Bradesco")
