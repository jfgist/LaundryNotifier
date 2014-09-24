# Script to log data from 4 sensors connected to an Arduino over serial.  It is intended to be 
# run from a Raspberry Pi and connected directly to the TX and RX pins on the Arduino Pro and Pi.

# adopted from http://www.scienceandsums.com/wp-content/uploads/2014/04/logData.txt

import sys, serial, time
from Utils import *

# set the serial port for the Arduino
serPort = '/dev/ttyAMA0' # rx and tx pins of the Raspberry Pi (use '/dev/ttyACM0' for the USB connection)

logFile1 = open ("./log1.dat","w");
logFile2 = open ("./log2.dat","w");
logFile3 = open ("./log3.dat","w");
logFile4 = open ("./log4.dat","w");
delay = 0.5

print "\n************************************"
print "\nLog Data"
print "\nAttempting to open serial port: ", serPort," for logging\n"

ser = serial.Serial(serPort,9600,timeout=1)

#check if port is open
if (ser.isOpen() == False):
	print "ERRROR: Uanble to open serial port\n"
	exit(0);
else: 
	print "Port Opened"
	
# force print to console
sys.stdout.flush()

# waits for signal from user to start logging
print "Hit return to start logging ..."
key = sys.stdin.readline()

print "Logging Started. CTRL-C to stop\n"

while True:
	try:
		# read data from serial
		ser.write('1')
		line = ser.readline()
		print line
		logFile1.write(line)
		time.sleep(delay)

		ser.write('2')
		line = ser.readline()
		print line
		logFile2.write(line)
		time.sleep(delay)

		ser.write('3')
		line = ser.readline()
		print line
		logFile3.write(line)
		time.sleep(delay)
		
		ser.write('4')
		line = ser.readline()
		print line
		logFile4.write(line)
		
		time.sleep(delay)
				
	except KeyboardInterrupt: #CTRL-C triggered here
	
		print "Logging Stopped\n"
		break;
	except serial.serialutil.SerialException:
		print "SerialException"
		pass
		
# close the serial port
ser.flush()
ser.close()
				
#close the Log File(s)
logFile1.close()
logFile2.close()
logFile3.close()
logFile4.close()

print "Port ",serPort," closed\n"
print "\n********************************************************\n"

print "\nPlot graph(s) (y/n) ?"
key = sys.stdin.read(1)
if key=='y':

    print "\nPlotting graph ...\n"

    # read all of the data from the textfile
    f = open("log1.dat",'r')
    lines = f.readlines()
    f.close()
    plot(lines)

    f = open("log2.dat",'r')
    lines = f.readlines()
    f.close()
    plot(lines)

    f = open("log3.dat",'r')
    lines = f.readlines()
    f.close()
    plot(lines)

    f = open("log4.dat",'r')
    lines = f.readlines()
    f.close()
    plot(lines)
	
    print "Plot complete\n"   

else:

    print "Finishing\n"



