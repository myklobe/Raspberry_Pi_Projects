import RPi.GPIO as GPIO
import time
import random
from random import randint
import decimal


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# This is where you define which GPIOs you want your LEDs 
# to be connected to on the Raspberry Pi
GPIO.setup(18,GPIO.OUT) # I used 18 for my Red LED
GPIO.setup(23,GPIO.OUT) # I used 23 for my Green LED
GPIO.setup(24,GPIO.OUT) # I used 24 for my Yellow LED

# I made a random sleeper program to mix up the times between lighting the LEDs
# You can use simple time.sleep(num) instead, but this is something I wanted to play with
def randomSleeper():
	num = random.uniform(0.1,3.0)
	num = float(num)
	time.sleep(num)
	print(num)

def redLEDOn():
	print('Red LED On')
	GPIO.output(18,GPIO.HIGH) # High turns the LED On

def redLEDOff():
	print('Red LED Off')
	GPIO.output(18,GPIO.LOW) # Low turns the LED Off

def greenLEDOn():
	print('Green LED On')
	GPIO.output(23,GPIO.HIGH) # High turns the LED On

def greenLEDOff():
	print('Green LED Off')
	GPIO.output(23,GPIO.LOW) # Low turns the LED Off

def yellowLEDOn():
	print('Yellow LED On')
	GPIO.output(24,GPIO.HIGH) # High turns the LED On

def yellowLEDOff():
	print('Yellow LED On')
	GPIO.output(24,GPIO.LOW) # Low turns the LED Off
