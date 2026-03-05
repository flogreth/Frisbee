## ----------  Servo Motor --------- ##
#   tested with tinkertanks frisbee   #

import time, board, pwmio
from adafruit_motor import servo

pwm = pwmio.PWMOut(board.GP12, duty_cycle=2**15, frequency=50)
my_servo = servo.Servo(pwm)

while True:
    my_servo.angle = 180
    time.sleep(0.5)
    my_servo.angle = 0
    time.sleep(0.5)