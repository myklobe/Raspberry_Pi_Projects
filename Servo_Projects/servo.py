import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
p = GPIO.PWM(7,50)
p.start(7.5)

try:
	while True:
		p.ChangeDutyCycle(7.5)	# Moves the servo to the neutral position
		print "Neutral"
		time.sleep(2)
		
		p.ChangeDutyCycle(12.5)	# Moves the servo to the 180 degrees position
		print "180 degrees"
		time.sleep(2)
		
		p.ChangeDutyCycle(2.5)	# Moves the servo to the 0 degrees position
		print "0 degrees"
		time.sleep(2)

except KeyboardInterrupt: # You can CTRL+C out of the program here.
	GPIO.cleanup()
