from flask import Flask, render_template, request
from gpiozero import Servo
from typing import Final

app = Flask(__name__)

# --- Configuration ---
# gpiozero uses BCM numbering by default.
# Physical Pin 7 = BCM 4
# Physical Pin 11 = BCM 17
PWM_PIN1: Final[int] = 4
PWM_PIN2: Final[int] = 17

# --- GPIO Setup ---
# gpiozero handles the PWM setup and frequency (50Hz) automatically
servo1 = Servo(PWM_PIN1)
servo2 = Servo(PWM_PIN2)

# --- Routes ---

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/move')
def move():
    # Get parameters from the URL
    servo_num = request.args.get('servo')
    angle = request.args.get('angle')

    # Map angle to gpiozero servo values (-1.0 to 1.0)
    # -1.0 = 0 degrees, 0.0 = 90 degrees, 1.0 = 180 degrees
    value_map = {
        "0": -1.0,
        "45": -0.5,
        "90": 0.0,
        "135": 0.5,
        "180": 1.0
    }

    value = value_map.get(angle)

    if value is not None:
        if servo_num == "1":
            servo1.value = value
        elif servo_num == "2":
            servo2.value = value
        elif servo_num == "both":
            servo1.value = value
            servo2.value = value

    return f"Moved Servo {servo_num} to {angle}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)