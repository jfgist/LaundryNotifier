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
GPIO.setup(18,GPIO.IN)

# Change to your own account information
to = 'james.gist@gmail.com'
gmail_user = 'raspberrypi1409@gmail.com'
gmail_password = ''
today = datetime.date.today()

buttonPressed = False

while True:
  #take a reading
  input = GPIO.input(18)
  print("Input: ")
  print(input)
  print("IsButton Pressed:")
  print(buttonPressed)
  time.sleep(0.1)
  
  if(input and not(buttonPressed)):
    print('Button Pressed')
    buttonPressed = True
    buttonPressTime = time.time()
    time.sleep(1)

  if (buttonPressed):
    time.sleep(60)
    if ((time.time() - buttonPressTime) > 3600):
      print("Send Email")
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
      
      buttonPressed = False



