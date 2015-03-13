
import RPi.GPIO as GPIO            ## Import GPIO Library
import time                        ## Import 'time' library (for 'sleep')
 
blue = 7                           
red = 11

GPIO.setmode(GPIO.BOARD)            ## Use BOARD pin numbering

## function to save code
def activateLED( pin, delay ):
	GPIO.setup(pin, GPIO.OUT)   ## set output
	GPIO.output(pin, GPIO.HIGH) ## set HIGH (LED ON)
	time.sleep(delay)	    ## wait  
	GPIO.output(pin, GPIO.LOW)  ## set LOW (LED OFF)
	return;

## light up blue
#activateLED(blue)
## light up red
#activateLED(red)

## Do a repeating show
ourRange = range(1,10)

for count in ourRange:
	activateLED(blue,.1)
	activateLED(red,.1)

GPIO.cleanup()                      ## close down library
