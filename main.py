'''
 Created by Barry Shichen Hu on March 11, 2022

 This program is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.
'''
from dataloader import Dataloader
# path to the project folders
project_folder = "/home/barry/dev/fintech"
data_folder = f"{project_folder}/data"

# 1. write a Loader class which loads the csv files into pandas Dataframes
# load the csv files
btc = Dataloader(f"{data_folder}/btc-usdt_20210115.csv", "btc-usdt")
eth = Dataloader(f"{data_folder}/eth-usdt_20210115.csv", "eth-usdt")
matic = Dataloader(f"{data_folder}/matic-usdt_20210115.csv", "matic-usdt")

# 2. Aggregate the trade data for each market to 1 minute candles (open, high, low, close, volume_base, volume_quote)
btc_ohlcv = btc.candle_stick()
eth_ohlcv = eth.candle_stick()
matic_ohlcv = matic.candle_stick()
# uncomment to visilize ohlc
# btc.ohlc_visualize()
# eth.ohlc_visualize()
# matic.ohlc_visualize()


# 3. Calculate the Relative Strength Index on a period of 20 minutes
btc_rsi = btc.rsi()
eth_rsi = eth.rsi()
matic_rsi = matic.rsi()
# uncomment to visilize rsi
# btc.rsi_visualize()
# eth.rsi_visualize()
# matic.rsi_visualize()


# 4. Calculate the Moving Average Convergence Divergence (12 minutes / 26 minutes / 9 minutes)
btc_macd = btc.macd()
eth_macd = eth.macd()
matic_macd = matic.macd()
# uncomment to visilize macd
# btc.macd_visualize()
# eth.macd_visualize()
# matic.macd_visualize()


# 5. Calculate the Bollinger Bands with a standard deviation of 3 on a period of 20 minutes

# Many traders believe the closer the prices move to the upper band, the more overbought the market, and the closer the prices move to the lower band, the more oversold the market.
btc_bollinger = btc.bollinger()
eth_bollinger = eth.bollinger()
matic_bollinger = matic.bollinger()
# uncomment to visilize macd
# btc.bollinger_visualize()
# eth.bollinger_visualize()
# matic.bollinger_visualize()


# 6. Plot the results and interpret the indicators
#     i. What do the indicators tell you and how can they generally be used to assess the market?
#     ii. How do the markets compare to each other?