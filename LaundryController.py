import subprocess
import smtplib
import socket
from email.mime.text import MIMEText
import RPi.GPIO as GPIO
import datetime
import time
import sys

#GPIO Setup
print("GPIO Setup")
inputPin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(inputPin,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
logFile = open("./log1.dat","w");


# Setup email timer delay
delay = 3 # default to one hour
print delay

if len(sys.argv) > 1:
  print delay
  print('here')
  delay = int(sys.argv[1])

print(delay)

# read the to email, from email and from password from config file
emailConfigFile ='/home/pi/tools/email.conf'
params = [line.strip() for line in open(emailConfigFile)]

if len(params) >= 3:
  to = params[0]
  gmail_user = params[1]
  gmail_password = params[2]

print(to)
print(gmail_user)
print(gmail_password)

today = datetime.date.today()
buttonPressed = False

dateString = '%H:%M:%S'

while True:
  #take a reading
  input = GPIO.input(inputPin)
  line = str(input) +"," + datetime.datetime.now().strftime(dateString)
  print(line)
  logFile.write(line+ '\n')
  time.sleep(0.5)
 
#  if(input and not(buttonPressed)):
#    print('Button Pressed First')
#    time.sleep(1)
#    input = GPIO.input(inputPin)
#    if (input):
#      print("Button held for X seconds")
#      #buttonPressed = True
#      buttonPressTime = time.time()
#    else:
#      print("Button Not Held Down")
#    time.sleep(1)

  if (buttonPressed):
    print("Button Pressed True")
    print((time.time()) - buttonPressTime)
    print(delay)
    if ((time.time() - buttonPressTime) > delay):
      print("Send Email")
      msg = MIMEText('ROTATE YOUR LAUNDRY')
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



