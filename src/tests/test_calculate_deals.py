from trade_bot.calculate_deals import find_buys_and_sells


def test_calculate_deals():
  buys, sells = find_buys_and_sells()

  assert len(set(buys).intersection(set(sells))) == 0