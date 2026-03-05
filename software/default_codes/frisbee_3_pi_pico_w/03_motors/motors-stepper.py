## --------  Stepper Motor --------- ##
#   tested with tinkertanks frisbee   #

# VERKABELUNG:    0<->pink     1<->ORANGE      3<->YELLOW    4<->BLUE     GND<->RED

import time, board, digitalio
from tt_stepper import Stepper

my_stepper = Stepper(2048) #2048 steps per rotation
print(my_stepper.position) #get the position

while True:
    for i in range (4):
        my_stepper.move_relative(42)	# 4 mal 42 grad drehen (relativ)
        time.sleep(0.5)
    my_stepper.move_to(0)				# zurück auf position 0 (absolut)
    time.sleep(1)

# all functions explained
my_stepper.move_to(540, speed = 100, accel= 100)    	# max-speed is 100   max-acceleration is 100 (0 is without smooth acceleration)
my_stepper.move_relative(540, speed = 100, accel= 100)  # relative
my_stepper.position()									# get stepper position
my_stepper.disable()									# disable steppers
print(my_stepper.position)
