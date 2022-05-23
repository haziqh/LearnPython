# Raw package
import numpy as np
import pandas as pd

#Data Source
import yfinance as yf

#Data viz library
import plotly.graph_objs as go

#Download AUD/MYR data
data = yf.download(tickers = 'AUDMYR=X' ,period ='1d', interval = '15m')

#declare figure
fig = go.Figure()

#Candlestick
fig.add_trace(go.Candlestick(x=data.index,
                open=data['Open'],
                high=data['High'],
                low=data['Low'],
                close=data['Close'], name = 'market data'))

# Add titles
fig.update_layout(
    title='Australian Dollar/Malaysian Ringgit')

#Show
fig.show()