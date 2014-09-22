LaundryNotifier
===============
Raspberry Pi/Arduino Project for notifying me when my laundry is done.

The current plan is to use one of the vibration sensors from SparkFun to characterize my washer and dryer with an Arduino/RPi setup and have the Pi text me when the laundry is done.  There's more than one way to skin this cat, but this it the way I am going to try.

- [ ] Check out vibration sensor documentation
- [ ] Update IDE with FTDI driver https://learn.sparkfun.com/tutorials/how-to-install-ftdi-drivers
- [ ] Order vibration sensor(s)
- [ ] Prototype Arduino/Raspberry Pi Communication
  - [ ] USB
  - [ ] SPI or I2C
- [ ] Characterize Appliances
  - [ ] Dryer
  - [ ] Washer
  - [ ] View/plot both of these on the Pi


Motivation
==========

The buzzer on my washing machine is ridiculously loud so I usually just turn it off...but then I forget about my laundry and may have to wash it again if is sits too long.  Hopefully the notification on my cell phone will be a better reminder.
