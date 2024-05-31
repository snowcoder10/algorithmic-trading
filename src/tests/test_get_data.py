from trade_bot.get_data import get_closing_data, get_tickers


def test_get_tickers():
  tickers = get_tickers()
  assert len(tickers) > 100
  assert "AAPL" in tickers

def test_get_closing_data():
  closings = get_closing_data("AAPL", 365)

  # account for weekends
  assert len(closings) == 251