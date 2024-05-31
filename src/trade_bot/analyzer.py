import os
from datetime import date
from trade_bot.calculate_deals import find_buys_and_sells
from trade_bot.email_utils import send_email

def send_trades_email():
  buys, sells = find_buys_and_sells()
  
  msg = f"Buy: {buys}\nSell: {sells}"
  to = os.environ['EMAIL_TO']
  sender = os.environ['EMAIL_FROM']
  today = date.today()
  subject = "Trades for " + today.strftime("%Y-%m-%d")

  send_email(to=to, sender=sender, subject=subject, body=msg, password=os.environ['EMAIL_PASSWORD'])

if __name__ == "__main__":
  send_trades_email()

  print("Trades sent!")