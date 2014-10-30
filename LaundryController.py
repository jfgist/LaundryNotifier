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
to = 'james.gist@gmail.com'
gmail_user = 'raspberrypi1409@gmail.com'
gmail_password = ''
smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(gmail_user, gmail_password)
today = datetime.date.today()
# Very Linux Specific
#msg = MIMEText(my_ip)

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
    prev_input = input
    msg = MIMEText('Content')
    msg['Subject'] = 'Message from RaspberryPi on %s' % today.strftime('%b %d %Y')
    msg['From'] = gmail_user
    msg['To'] = to
    smtpserver.sendmail(gmail_user, [to], msg.as_string())
    smtpserver.quit()

    #slight pause to debounce
    time.sleep(0.5)
    prev_input = 0
    


