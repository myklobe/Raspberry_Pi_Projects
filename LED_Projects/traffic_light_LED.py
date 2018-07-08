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
	setupLED.redLEDOn()
	time.sleep(5000)
	setupLED.redLEDOff()

	setupLED.yellowLEDOn()
	time.sleep(2000)
	setupLED.yellowLEDOff()
	
	setupLED.greenLEDOn()
	time.sleep(5000)
	setupLED.greenLEDOff()
	i += 1