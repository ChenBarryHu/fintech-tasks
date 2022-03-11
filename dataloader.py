'''
 Created by Barry Shichen Hu on March 11, 2022

 This program is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.
'''
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import os

class Dataloader:
    """Data loading and analyzation class"""
    def __init__(self, path, market):
        if not os.path.exists(path):
            raise Exception(f'invalid path: {path}')
        self.df = pd.read_csv(path, parse_dates=True)
        self.df = self.df.rename(columns={"amount":"base_amount"})
        self.df['date'] = pd.to_datetime(self.df['date'])
        self.df['quote_amount'] = self.df['base_amount'] * self.df['price']
        self.market = market

        # always generate the ohlcv data frame since all other data aggregation depend on the ohlcv. 
        self.candle_stick()

    def candle_stick(self, freq="1min"):
        """
        Compute the ohlcv(open, high, low, close, volumn) data frame
        """
        df_f = self.df.groupby([pd.Grouper(key='date', freq=freq)])\
            .agg(open=pd.NamedAgg(column='price', aggfunc='first'), 
              close=pd.NamedAgg(column='price', aggfunc='last'), 
              high=pd.NamedAgg(column='price', aggfunc='max'), 
              low=pd.NamedAgg(column='price', aggfunc='min'),
              volumn_base=pd.NamedAgg(column='base_amount', aggfunc='sum'),
              volumn_quote=pd.NamedAgg(column='quote_amount', aggfunc='sum'))\
            .reset_index()
        self.ohlcv = df_f
        return df_f

    def ohlc_visualize(self):
        """
        Visualize the ohlcv data frame
        """
        self.ohlcv['date'] = pd.to_datetime(self.ohlcv['date'])
        fig = go.Figure(data=[go.Candlestick(x=self.ohlcv['date'],
                open=self.ohlcv['open'],
                high=self.ohlcv['high'],
                low=self.ohlcv['low'],
                close=self.ohlcv['close'])])

        fig.show()

    def bollinger(self, window_length=20, n_std=3):
        """
        Computes the Moving Average Convergence Divergence (12 minutes / 26 minutes / 9 minutes)
        based on https://www.alpharithms.com/calculate-macd-python-272222/#:~:text=The%20Moving%20Average%20Convergence%20Divergence%20is%20a%20momentum%20indicator%20that,%2C%20momentum%2C%20and%20possible%20breakouts. 
        """
        tp = (self.ohlcv['close'] + self.ohlcv['low'] + self.ohlcv['high'])/3
        self.bollinger = pd.DataFrame(tp).rename(columns = {0:'tp'}).set_index(self.ohlcv['close'].index)
        sma = tp.rolling(window=window_length).mean()
        std = tp.rolling(window=window_length).std()
        bollinger_up = sma + std * n_std # Calculate top band
        bollinger_down = sma - std * n_std # Calculate bottom band
        self.bollinger["sma"] = sma
        self.bollinger["std"] = std
        self.bollinger["bollinger_up"] = bollinger_up
        self.bollinger["bollinger_down"] = bollinger_down
        self.bollinger["close"] = self.ohlcv["close"]
        return self.bollinger
    
    def bollinger_visualize(self):
        """
        Visualize the bollinger band of the asset
        """
        ax = self.bollinger[['close','bollinger_up', 'bollinger_down']].plot(color=['blue','orange', 'yellow'])
        ax.set_title(f'{self.market} Bollinger Band')
        ax.fill_between(self.bollinger.index, self.bollinger['bollinger_up'], self.bollinger['bollinger_down'], facecolor='grey', alpha=0.1)
        plt.show()
        

    def macd(self):
        """
        Computes the Moving Average Convergence Divergence (12 minutes / 26 minutes / 9 minutes)
        based on https://www.alpharithms.com/calculate-macd-python-272222/#:~:text=The%20Moving%20Average%20Convergence%20Divergence%20is%20a%20momentum%20indicator%20that,%2C%20momentum%2C%20and%20possible%20breakouts. 
        """
        if self.ohlcv is None:
            self.candle_stick()
        k = self.ohlcv['close'].ewm(span=12, adjust=False, min_periods=12).mean()
        # Get the 12-day EMA of the closing price
        d = self.ohlcv['close'].ewm(span=26, adjust=False, min_periods=26).mean()
        # Subtract the 26-day EMA from the 12-Day EMA to get the MACD
        macd = k - d
        
        # Get the 9-Day EMA of the MACD for the signal line
        macd_s = macd.ewm(span=9, adjust=False, min_periods=9).mean()
        # Calculate the difference between the MACD - Trigger for the Convergence/Divergence value
        macd_h = macd - macd_s
        # Add all of our new values for the MACD to the dataframe
        self.macd = pd.DataFrame(macd).rename(columns = {0:'macd'}).set_index(self.ohlcv['close'].index)
        self.macd = self.macd.rename(columns={"close":"macd"})
        # self.macd['macd'] = self.ohlcv.index.map(macd)
        self.macd['macd_h'] = macd_h
        self.macd['signal'] = macd_s
        self.macd["date"] = self.ohlcv["date"]
        return self.macd

    def macd_visualize(self):
        """Visualization of the macd graph"""
        plt.plot(self.macd["macd"], label='MACD', linewidth = 1.5, color = 'skyblue')
        plt.plot(self.macd["signal"], label='Signal Line', linewidth = 1.5, color='orange')
        plt.legend(loc='upper left')
        plt.title(f'{self.market} MACD')
        plt.show()


    def rsi(self, window_length=20):
        """
        Compute the relative strength index for the market, 
        based on https://medium.com/codex/algorithmic-trading-with-relative-strength-index-in-python-d969cf22dd85 
        """
        if self.ohlcv is None:
            self.candle_stick()
        ret = self.ohlcv['close'].diff()
        gain = []
        loss = []
        for i in range(len(ret)):
            if ret[i] < 0:
                gain.append(0)
                loss.append(abs(ret[i]))
            else:
                gain.append(ret[i])
                loss.append(0)
        gain_series = pd.Series(gain)
        loss_series = pd.Series(loss)
        gain_ewm = gain_series.ewm(com = window_length - 1, adjust = False).mean()
        loss_ewm = loss_series.ewm(com = window_length - 1, adjust = False).mean()
        rs = gain_ewm/loss_ewm
        rsi = 100 - (100 / (1 + rs))
        rsi_df = pd.DataFrame(rsi).rename(columns = {0:'rsi'}).set_index(self.ohlcv['close'].index)
        rsi_df = rsi_df.dropna()
        rsi_df["date"] = self.ohlcv["date"]
        self.rsi = rsi_df
        return rsi_df

    def rsi_visualize(self):
        """
        Visualize the closing price and RSI for the market, 
        based on https://medium.com/codex/algorithmic-trading-with-relative-strength-index-in-python-d969cf22dd85 
        """
        if self.ohlcv is None:
            self.candle_stick()
        # ax1 = plt.subplot2grid((10,1), (0,0), rowspan = 4, colspan = 1)
        # ax2 = plt.subplot2grid((10,1), (5,0), rowspan = 4, colspan = 1)
        # ax1.plot(self.ohlcv['close'], linewidth = 1.5, color = 'skyblue', label = 'IBM')
        # ax1.plot(ibm.index, buy_price, marker = '^', markersize = 10, color = 'green', label = 'BUY SIGNAL')
        # ax1.plot(ibm.index, sell_price, marker = 'v', markersize = 10, color = 'r', label = 'SELL SIGNAL')
        ax = self.rsi['rsi'].plot(color='orange', linewidth=1.5)
        ax.set_title(f'{self.market} RSI')
        # ax.plot(self.rsi['rsi'], color = 'orange', linewidth = 1.5)
        ax.axhline(30, linestyle = '--', linewidth = 1.5, color = 'grey')
        ax.axhline(70, linestyle = '--', linewidth = 1.5, color = 'grey')
        plt.show()