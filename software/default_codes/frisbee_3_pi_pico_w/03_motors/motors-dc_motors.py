## --------  Stepper Motor --------- ##
#   tested with tinkertanks frisbee   #

import time, board, pwmio, digitalio
from adafruit_motor import motor

# OUTPUT 1
M1_A = board.GP0
M1_B = board.GP1
motor1 = motor.DCMotor(pwmio.PWMOut(M1_A, frequency=50), pwmio.PWMOut(M1_B, frequency=50))

while True:
    motor1.throttle = -1		# rückwärts Vollgas
    time.sleep(2)
    motor1.throttle = 0.5		# vorwärts halb
    time.sleep(2)
    motor1.throttle = 0			# aus
    time.sleep(2)