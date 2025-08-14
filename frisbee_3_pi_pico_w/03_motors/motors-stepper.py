## --------  Stepper Motor ---------- ##
#   tested with tinkertanks frisbee   #

import time, board, digitalio
from tt_stepper import Stepper

my_stepper = Stepper(2048) #2048 steps per rotation


# Rotate Stepper 1 full turn in each direction, pausing 30 sec between directions



print(my_stepper.position) #get the position

while True:	
    my_stepper.move_to(540, 200, 200)
    print(my_stepper.position)
    time.sleep(1)
    my_stepper.move_to(0)
    print(my_stepper.position)
    time.sleep(1)


# explanation

my_stepper.move_to(540, speed = 100, accel= 100)    	# max-speed is 100   max-acceleration is 100 (0 is without smooth acceleration)
my_stepper.move_relative(540, speed = 100, accel= 100)  # relative
my_stepper.position()									# get stepper position
my_stepper.disable()									# disable steppers


print(my_stepper.position)