# Raw package
import numpy as np
import pandas as pd

#Data Source
import yfinance as yf

#Data viz library
import plotly.graph_objs as go

currency_1 = input('Currency 1: ')
currency_2 = input('Currency 2: ')
selected_period = input('Choose period to view (1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max): ')
selected_interval = input('Choose interval (1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo): ')

final_currency_input = str(currency_1 + currency_2 + '=X')
final_selected_input = str(selected_period)
final_interval = str(selected_interval)

#Download currency_1/currency_2 data
data = yf.download(tickers = final_currency_input ,period =final_selected_input, interval = final_interval)

#declare figure
fig = go.Figure()

#Candlestick
fig.add_trace(go.Candlestick(x=data.index,
                open=data['Open'],
                high=data['High'],
                low=data['Low'],
                close=data['Close'], name = 'market data'))

# Add titles
title_graph = str(currency_1.upper()) + '/' + str(currency_2.upper())

fig.update_layout(
    title=title_graph)

#Show
fig.show()