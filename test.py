# Raspberry Pi LED Demo
#
# Jeremy Morgan
# 3-12-15


import RPi.GPIO as GPIO            	## Import GPIO Library
import time                        	## Import 'time' library (for 'sleep')

blue = 15							## These are our LEDs
red = 7
yellow = 7
green = 13

red2 = 40
yellow2 = 38
blue2 = 32
green2 = 36

GPIO.setmode(GPIO.BOARD)            ## Use BOARD pin numbering

## function to save code

def activateLED( pin, delay ):
	GPIO.setup(pin, GPIO.OUT)   	## set output
	GPIO.output(pin, GPIO.HIGH) 	## set HIGH (LED ON)
	time.sleep(delay)	    		## wait
	GPIO.output(pin, GPIO.LOW)
	#time.sleep(delay)	  	## set LOW (LED OFF)
	return;


## Manual light
'''
GPIO.setup(blue, GPIO.OUT)   	## set output
GPIO.output(blue, GPIO.HIGH) 	## set HIGH (LED ON)
time.sleep(1)	    			## wait
GPIO.output(blue, GPIO.LOW)  	## set LOW (LED OFF)
'''
## light up blue
#activateLED(blue,.1)
## light up red
#activateLED(red,.1)

## Do a repeating show!
ourRange = range(1,10)

ourdelay = .1
herdelay = .1

#first dance

'''
for count in ourRange:
	activateLED(red,ourdelay)
	activateLED(red2,ourdelay)
	activateLED(yellow,ourdelay)
	activateLED(yellow2,ourdelay)
	activateLED(green,ourdelay)
	activateLED(green2,ourdelay)
	activateLED(blue,ourdelay)
	activateLED(blue2,ourdelay)

for count in ourRange: 
	activateLED(red,ourdelay)
	activateLED(yellow,ourdelay)
	activateLED(green,ourdelay)
	activateLED(blue,ourdelay)
	activateLED(red2,ourdelay)
	activateLED(yellow2,ourdelay)
	activateLED(green2,ourdelay)
	activateLED(blue2,ourdelay)

for count in ourRange:
	activateLED(red,ourdelay)
	activateLED(red2,ourdelay)
	activateLED(yellow,ourdelay)
	activateLED(yellow2,ourdelay)
	activateLED(green,ourdelay)
	activateLED(green2,ourdelay)
	activateLED(blue,ourdelay)
	activateLED(blue2,ourdelay)

for count in ourRange: 
	activateLED(red,ourdelay)
	activateLED(yellow,ourdelay)
	activateLED(green,ourdelay)
	activateLED(blue,ourdelay)
	activateLED(red2,ourdelay)
	activateLED(yellow2,ourdelay)
	activateLED(green2,ourdelay)
	activateLED(blue2,ourdelay)

'''

for count in ourRange: 
	activateLED(red,herdelay)
	activateLED(red,ourdelay)
	activateLED(yellow,herdelay)
	activateLED(yellow,ourdelay)
	activateLED(green,herdelay)
	activateLED(green,ourdelay)
	activateLED(blue,herdelay)
	activateLED(blue,ourdelay)
	activateLED(red2,herdelay)
	activateLED(red2,ourdelay)
	activateLED(yellow2,herdelay)
	activateLED(yellow2,ourdelay)
	activateLED(green2,herdelay)
	activateLED(green2,ourdelay)
	activateLED(blue2,herdelay)
	activateLED(blue2,ourdelay)

for count in ourRange: 
	activateLED(red,herdelay)
	activateLED(red,ourdelay)
	activateLED(yellow,herdelay)
	activateLED(yellow,ourdelay)
	activateLED(green,herdelay)
	activateLED(green,ourdelay)
	activateLED(blue,herdelay)
	activateLED(blue,ourdelay)
	activateLED(red2,herdelay)
	activateLED(red2,ourdelay)
	activateLED(yellow2,herdelay)
	activateLED(yellow2,ourdelay)
	activateLED(green2,herdelay)
	activateLED(green2,ourdelay)
	activateLED(blue2,herdelay)
	activateLED(blue2,ourdelay)

GPIO.cleanup()                      ## close down library
