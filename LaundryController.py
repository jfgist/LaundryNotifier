import subprocess
import smtplib
import socket
from email.mime.text import MIMEText
import RPi.GPIO as GPIO
import datetime
import time

#GPIO Setup
print("GPIO Setup")
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN)

# Change to your own account information
to = '@gmail.com'
gmail_user = 'raspberrypi1409@gmail.com'
gmail_password = ''
today = datetime.date.today()

prev_input = 0;
while True:
  #take a reading
  input = GPIO.input(17)
  print("Input: ")
  print(input)
  time.sleep(0.1)
  #if reading went from low to high
  if((not prev_input) and input):
    print("Button Pressed")
    time.sleep(3600)
    prev_input = input
    msg = MIMEText('ROTATE YO LAUNDRY')
    msg['Subject'] = 'Pi-Notify on %s' % today.strftime('%b %d %Y')
    msg['From'] = gmail_user
    msg['To'] = to
    smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(gmail_user, gmail_password)
    smtpserver.sendmail(gmail_user, [to], msg.as_string())
    smtpserver.close()

    #slight pause to debounce
    time.sleep(0.5)
    prev_input = 0
    


