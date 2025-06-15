## ----  Ultrasonic Distance Sensor  ---- ##
#     tested with tinkertanks frisbee      #

import time, board, adafruit_hcsr04, digitalio

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.GP12, echo_pin=board.GP13)

while True:
    try:
        print((sonar.distance,))
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)