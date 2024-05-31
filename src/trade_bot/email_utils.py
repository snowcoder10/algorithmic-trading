import smtplib
from email.mime.text import MIMEText
import os

def send_email(to, sender, password, subject, body):
  msg = MIMEText(body)

  # me == the sender's email address
  # you == the recipient's email address
  msg['Subject'] = subject
  msg['From'] = sender
  msg['To'] = to

  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.starttls()
  server.login(sender, password)
  server.sendmail(sender, [to], msg.as_string())
  server.quit()