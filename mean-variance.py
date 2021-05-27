import os
import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from MCForecastTools import MCSimulation
import panel as pn
import seaborn as sns
import streamlit as st


st.write("""
### Test Mean-Variance Optimization
""")

st.markdown (""" This app performs....""")
# https://github.com/robertmartin8/PyPortfolioOpt/blob/master/cookbook/2-Mean-Variance-Optimisation.ipynb
#choose the tickers of stocks and cryptos in our list
tickers = ["AMC", "AMD", "BABA", "BB", "BBBY", 
           "GME", "MVIS", "NVDA", "TSLA", "SPY"]
#get data on this ticker
data = yf.download(tickers, period="4y",interval="1d",auto_adjust=True, prepost=True,threads=True,proxy=None)
prices = data["Adj Close"].dropna(how="all")
st.line_chart(prices.Close)
st.line_chart(prices.Volume)
st.sidebar.header ("user selection")
selected_investments = st.sidebar.selectbox (tickers)