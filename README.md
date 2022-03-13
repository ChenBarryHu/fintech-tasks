# To execute the code
1. install dependencies.
```shell
pip install pandas plotly matplotlib
```
2. under the project folder, create a data folder:
```shell
mkdir data
```
and download the data files into this data folder.      
3. update the project folder path (in main.py line 11) to the correct one.      
4. under the project folder, run:
```shell
python main.py
```

# fintech-tasks
## 1. Candle chart with 1 minute period (open, high, low, close, volume_base, volume_quote)
**how can the indicator generally be used to assess the market?**
The Open-High-Low-Close(OHLC)/Candle chart shows increasing or decreasing momentum:
When the open and close are far apart it shows strong momentum, and when the open and close are close together it shows indecision or weak momentum. The high and low are useful in assessing volatility.      

**What do the indicators tell you about the markets and how do the markets compare to each other?** 
1. first of all, for all markets the green candles and the red candles are interwoven, which means the markets are high unstable over the 24 hour period.
2. around 15:00 to 16:00, all three markets witnessed series of red bars (indication of oversold). Thus in this one hour period, all three markets show a downward momentom, resulting in great price decrease.
3. i would say it is hard to compare the three markets based on the OHLC charts except the obvious price changes.     

i) BTC
![BTC_OHLC](https://github.com/ChenBarryHu/fintech-tasks/blob/master/images/BTC_OHLC.png)
ii) ETH
![ETH_OHLC](https://github.com/ChenBarryHu/fintech-tasks/blob/master/images/ETH_OHLC.png)
iii) Matic
![ETH_OHLC](https://github.com/ChenBarryHu/fintech-tasks/blob/master/images/Matic_OHLC.png)

## 2. Relative Strength Index (RSI) on a period of 20 minutes
**how can the indicator generally be used to assess the market?**
The Relative Strength Index (RSI) describes the current price relative to average high and low prices over a previous trading period. This indicator estimates overbought or oversold status.      

WHen the RSI values are above a given threshold (commonly 70), this indicate an overbought market (time to sell!); and when the values are below a given threshold (commonly 30), this indicates an oversold market (time to buy!).     

**What do the indicators tell you about the markets and how do the markets compare to each other?**    
1. Interestingly, the buy-sell signals generated by the rsi values crossing the thresholds(30/70) roughly matches the price upward downward trend in OHLC charts above.
2. For Matic, the rsi values cross the thresholds more often, which means that for matic-usdt market, there are more overbought and oversold stages, thus more buy-sell opportunities to profit.    
3. For btc and eth, they tend to be oversold rather than being overbouht over the 24 hour period, because their rsi drop below 30 more often than exceeding 70.

i) BTC
![BTC_RSI](https://github.com/ChenBarryHu/fintech-tasks/blob/master/images/BTC_RSI.png)
ii) ETH
![ETH_RSI](https://github.com/ChenBarryHu/fintech-tasks/blob/master/images/ETH_RSI.png)
iii) Matic
![ETH_RSI](https://github.com/ChenBarryHu/fintech-tasks/blob/master/images/Matic_RSI.png)

## 3. Moving Average Convergence Divergence(MACD)
**how can the indicator generally be used to assess the market?**
MACD shows the relationship between two moving averages of a security’s price. The MACD is calculated by subtracting the 26-period exponential moving average (EMA) from the 12-period EMA. Thus, "0 line" is a baseline for comparing the two EMA, and the more distant the MACD is above or below its baseline indicates that the distance between the two EMAs is growing.   

A nine-day EMA of the MACD called the "signal line," is then plotted on top of the MACD line, which can function as a trigger for buy and sell signals. Traders may buy the security when the MACD crosses above its signal line and sell—or short—the security when the MACD crosses below the signal line. The speed of crossovers is also taken as a signal of a market is overbought or oversold.    

**What do the indicators tell you about the markets and how do the markets compare to each other?**      
1. For all three markets, the MACDs drops and rises rapidly, especially around 15:00-17:00, this shows that the three markets has significant oversold and overbought stages. 
2. For btc and eth markets, most of the time, the MACDs stay below 0, this indicats that for these two markets, price downward trends are more often than the upward trends. The Matic market looks more promising since its MACD stays above 0 more often than the other two markets.
3. All three market's MACDs cross their signal lines quite often, indicating the iterating oversold and overbought stages.    

i) BTC
![BTC_MACD](https://github.com/ChenBarryHu/fintech-tasks/blob/master/images/BTC_MACD.png)
ii) ETH
![ETH_MACD](https://github.com/ChenBarryHu/fintech-tasks/blob/master/images/ETH_MACD.png)
iii) Matic
![ETH_MACD](https://github.com/ChenBarryHu/fintech-tasks/blob/master/images/Matic_MACD.png)


## 4. Bollinger Band
**how can the indicator generally be used to assess the market?**
A common conprehension is that: For a Bollinger Band, the closer the prices move to the upper band, the more overbought the market (time to sell), and the closer the prices move to the lower band, the more oversold the market(time to buy).    

**What do the indicators tell you about the markets and how do the markets compare to each other?**     
1. for all of the three markets, there are times when the closing price approaches the upper and lower bounds, which means there are clear sell-buy signsls for all three markets.
2. it seems that btc and eth's close prices approach the lower bound more often than the upper bound, which could explain that their price dropped over the 24hour period; while for Matic, its close price approaches thr upper bound more often than the lower bound, and its price rises over the 24 hour period. Over this 24 hour, btc and eth tends to be oversold, while Matic tends to be overbought.     

i) BTC
![BTC_Bollinger](https://github.com/ChenBarryHu/fintech-tasks/blob/master/images/BTC_Bollinger.png)
ii) ETH
![ETH_Bollinger](https://github.com/ChenBarryHu/fintech-tasks/blob/master/images/ETH_Bollinger.png)
iii) Matic
![ETH_Bollinger](https://github.com/ChenBarryHu/fintech-tasks/blob/master/images/Matic_Bollinger.png)
