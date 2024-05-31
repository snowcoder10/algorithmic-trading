from pypm.signals import create_bollinger_band_signal, create_macd_signal
from trade_bot.get_data import get_closing_data_for_tickers


def find_buys_and_sells():
  closing_data = get_closing_data_for_tickers()
  buys= []
  sells = []

  for ticker, data in closing_data.items():
    macd_signal = create_macd_signal(data)
    bollinger_signal = create_bollinger_band_signal(data)
    if len(macd_signal) == 0 or len(bollinger_signal) == 0:
      continue
    elif macd_signal[-1] > 0 and (bollinger_signal[-1] > 0 or bollinger_signal[-1] == 0):
      buys.append(ticker)
    elif macd_signal[-1] < 0 and (bollinger_signal[-1] < 0 or bollinger_signal[-1] == 0):
      sells.append(ticker)

  return buys, sells
