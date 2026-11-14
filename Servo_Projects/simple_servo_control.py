import RPi.GPIO as GPIO
import time
from typing import Final

# Constants for configuration

# Servo 1 configuration
PWM_PIN7: Final[int] = 7
# Servo 2 configuration
PWM_PIN11: Final[int] = 11

PWM_FREQ: Final[int] = 50
DUTY_NEUTRAL: Final[float] = 7.5
DUTY_180: Final[float] = 12.5
DUTY_0: Final[float] = 2.5

def main() -> None:
    # Setup
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(PWM_PIN7, GPIO.OUT)
    GPIO.setup(PWM_PIN11, GPIO.OUT)

    # Initialize PWM for Servo 1
    p1 = GPIO.PWM(PWM_PIN7, PWM_FREQ)
    p1.start(DUTY_NEUTRAL)

    # Initialize PWM for Servo 2
    p2 = GPIO.PWM(PWM_PIN11, PWM_FREQ)
    p2.start(DUTY_NEUTRAL)

    print(f"Starting Dual Servo Control. Press CTRL+C to stop.")

    try:
        while True:
            # Move both to Neutral
            p1.ChangeDutyCycle(DUTY_NEUTRAL)
            p2.ChangeDutyCycle(DUTY_NEUTRAL)
            print("Both: Neutral")
            time.sleep(2)

            # Move both to 180 degrees
            p1.ChangeDutyCycle(DUTY_180)
            p2.ChangeDutyCycle(DUTY_180)
            print("Both: 180 degrees")
            time.sleep(2)

            # Move both to 0 degrees
            p1.ChangeDutyCycle(DUTY_0)
            p2.ChangeDutyCycle(DUTY_0)
            print("Both: 0 degrees")
            time.sleep(2)

    except KeyboardInterrupt:
        print("\nStopping program...")
    finally:
        # Stop both PWM objects
        p1.stop()
        p2.stop()
        # Cleanup GPIO
        GPIO.cleanup()
        print("GPIO Cleanup complete.")

if __name__ == "__main__":
    main()