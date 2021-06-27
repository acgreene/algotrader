import yfinance as yf
import requests
import numpy

data = yf.download("SPY", start="2000-01-01", end="2019-10-04")
data.to_csv("backtest/burns_200_day_crush/data/spy.csv")
