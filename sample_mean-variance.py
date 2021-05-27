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


header = st.beta_container()
dataset = st.beta_container()
investments = st.beta_container()
results = st.beta_container()

@st.cache
def get_data(filename):
    data = pd.read_csv(filename)
    
    return data

with header:
    st.title("Welcome to YOLO advisors Inc")


with dataset:
    st.header("Display current market performance")
    st.text("")
    
    data = get_data('crypto_prices.csv')
    st.write(data.head())

with investments:
    st.header("Universe of Stocks and Cryptos")
    st.text("Choose the companies you want to invest in")
    
    select_col, display_col = st.beta_columns(2)
    
    input_investment=select_col.selectbox('select investments',options=["BTC","ETH","ETC"])
    input_risk=display_col.slider('What is your risk tolerance?', min_value=1, max_value=100, value=20)
with results:
    st.header("Displays")
    

    ef_col, bl_col = st.beta_columns (2)
    
    ef_col.subheader("The Efficient Frontier for this porftolfio is:")
    bl_col.subheader("Here is a projected performance of the portfolio taking into consideration your views")