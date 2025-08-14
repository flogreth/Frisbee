import time, board, adafruit_hcsr04, digitalio, pwmio
from adafruit_motor import motor

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.GP12, echo_pin=board.GP13)
# OUTPUT 1
M1_A = board.GP0
M1_B = board.GP1
motor1 = motor.DCMotor(pwmio.PWMOut(M1_A, frequency=50), pwmio.PWMOut(M1_B, frequency=50))



while True:
    try:
        print((sonar.distance,))
        
        if sonar.distance < 10:
                print ("!!!")
                motor1.throttle = -1
                time.sleep(2)
                motor1.throttle = 1
                time.sleep(2)
                motor1.throttle = 0
                
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)
    
    
        
    
    