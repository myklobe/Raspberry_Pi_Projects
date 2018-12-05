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
# Random number between 0.1 and 3.0 seconds. Change these to meet your needs
# You can use simple time.sleep(num) instead, but I wanted to include a random sleep timer

def randomSleeper():
	num = random.uniform(0.1,3.0) # Can change these values to whatever range you want
	num = float(num)
	time.sleep(num)
	print(num) # printing randomSleeper value. Can comment out if you don't want an output

def redLEDOn():
	print('Red LED On') # printing LED state. Can comment out if you don't want an output
	GPIO.output(18,GPIO.HIGH) # High turns the LED On

def redLEDOff():
	print('Red LED Off') # printing LED state. Can comment out if you don't want an output
	GPIO.output(18,GPIO.LOW) # Low turns the LED Off

def greenLEDOn():
	print('Green LED On') # printing LED state. Can comment out if you don't want an output
	GPIO.output(23,GPIO.HIGH) # High turns the LED On

def greenLEDOff():
	print('Green LED Off') # printing LED state. Can comment out if you don't want an output
	GPIO.output(23,GPIO.LOW) # Low turns the LED Off

def yellowLEDOn():
	print('Yellow LED On') # printing LED state. Can comment out if you don't want an output
	GPIO.output(24,GPIO.HIGH) # High turns the LED On

def yellowLEDOff():
	print('Yellow LED On') # printing LED state. Can comment out if you don't want an output
	GPIO.output(24,GPIO.LOW) # Low turns the LED Off
