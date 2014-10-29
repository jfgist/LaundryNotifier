LaundryNotifier
===============
Raspberry Pi/Arduino Project for notifying me when my laundry is done.

The current plan is to use one of the vibration sensors from SparkFun to characterize my washer and dryer with an Arduino/RPi setup and have the Pi text me when the laundry is done.  There's more than one way to skin this cat, but this it the way I am going to try.

- [x] Check out vibration sensor documentation
- [x] Stub out python code to prompt arduino for values (use Serial)
- [x] Update IDE with FTDI driver https://learn.sparkfun.com/tutorials/how-to-install-ftdi-drivers
- [x] Order vibration sensor(s)
- [ ] Stopgap Solution (Timer)
  - [ ] Setup email http://elinux.org/RPi_Email_IP_On_Boot_Debian or http://rpi.tnet.com/project/faqs/smtp
  - [ ] Write code to listen for button press
  - [ ] Send text(email) in code
- [ ] Prototype Arduino/Raspberry Pi Communication
  - [ ] USB
  - [ ] SPI or I2C
  - [x] Direct serial
- [ ] Characterize Appliances (in progress, currently running against dummy sensor values, hitting some errors)
  - [ ] Dryer
  - [ ] Washer
  - [ ] View/plot both of these on the Pi


Motivation
==========

The buzzer on my washing machine is ridiculously loud so I usually just turn it off...but then I forget about my laundry and may have to wash it again if is sits too long.  Hopefully the notification on my cell phone will be a better reminder.


Dependencies
============
* matplotlib - sudo apt-get install python-matplotlib
* ssmtp
* mailutils
* mpack

Contents
========

- AnalogRead.ino - Arduino code to constantly read values from two sensors and return the value for one of them when the appropriate command is initiated over the serial connection.
- LaundryController.py - Main code for executing the functionality.  This will likely be populated with information gianed from running characterize
- Characterize.py - Generic method to gather sensor data and characterize the vibrations of the washer and dryer.
- Utils.py - currently just has the plot function for plotting the logged data.

Connections/Usage
=================

Connections Between the Pi and Arduino.
Vcc (3.3v) on the Arduino connects to the GPIO Vcc (3.3v) pin:    Pin #1.
Ground on the Arduino connects to the GPIO Ground pin:           Pin #6.
TxD on the Arduino connects to the GPIO RxD pin:                        Pin #10.
RxD on the Arduino connects to the GPIO TxD pin:                        Pin #8.

Upload AnalogRead.ino to the Arduino
Execute Characterize.py from the Raspberry Pi
