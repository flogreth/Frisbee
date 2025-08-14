import time, board, pwmio, digitalio
from adafruit_motor import motor

pin = digitalio.DigitalInOut(board.GP2)    	# GP0 instead of LED for Pin D0
pin.direction = digitalio.Direction.OUTPUT 	# set gpio pin to 'output's
pin.value = 1

# OUTPUT 1
M1_A = board.GP0
M1_B = board.GP1
motor1 = motor.DCMotor(pwmio.PWMOut(M1_A, frequency=50), pwmio.PWMOut(M1_B, frequency=50))


# OUTPUT 2
M2_A = board.GP3
M2_B = board.GP4
motor2 = motor.DCMotor(pwmio.PWMOut(M2_A, frequency=50), pwmio.PWMOut(M2_B, frequency=50))

while True:

    motor1.throttle = -1
    time.sleep(2)
    motor1.throttle = 1
    time.sleep(2)
    print(time.monotonic())

motor1.throttle = None