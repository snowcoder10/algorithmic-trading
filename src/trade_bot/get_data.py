import yfinance as yf
import pandas as pd
from datetime import timedelta
import json
import random

def get_closing_data_for_tickers():
  tickers = get_tickers()
  closing_data = {}

  for ticker in tickers:
    closing_data[ticker] = get_closing_data(ticker, 365)

  return closing_data

def get_closing_data(ticker: str, days_back=100) -> pd.Series:
  """
  Get the closing prices for a given stock ticker past year
  """
  # Get the data for the stock
  stock = yf.Ticker(ticker)

  # Get the historical data
  today = pd.Timestamp.today()
  start_date = today - timedelta(days=days_back)
  end_date = today

  # Fetch the historical data
  data = stock.history(start=start_date, end=end_date)

  # Get the closing prices for the requested period
  closing_prices = data["Close"]

  return closing_prices

def get_tickers():
  with open('trade_bot/tickers.json', 'rb') as file:
    data = json.load(file)

  qqq_tickers = data['qqq']
  sp500_tickers = data['spy']
  dji_tickers = data['dji']
  return set([*sp500_tickers, *dji_tickers, *qqq_tickers])