import RPi.GPIO as GPIO
import time
import random
import decimal
from random import randint
import simple_LED_blink_setup # This has my LED On/Off methods

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


i = 0
while i < 10: #Loops 10 times, but you can make cycle indefinitely or for a specific # of times
	setupLED.redLEDOn() # Red Light on for 5 seconds
	time.sleep(5000)
	setupLED.redLEDOff() # Red Light off

	setupLED.yellowLEDOn() # Yellow light on for 2 seconds
	time.sleep(2000)
	setupLED.yellowLEDOff() # Yellow light off
	
	setupLED.greenLEDOn() # Green light on for 5 seconds
	time.sleep(5000)
	setupLED.greenLEDOff() # Green light off
	i += 1
