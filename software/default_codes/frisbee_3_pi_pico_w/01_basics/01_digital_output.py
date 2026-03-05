## --------  LED (Digital Output)  ------- ##
#      tested with tinkertanks frisbee      #

import time, board, digitalio

pin = digitalio.DigitalInOut(board.GP12)    	# LED an Pin 12
pin.direction = digitalio.Direction.OUTPUT 		# Pin auf Output setzen

while True:
    pin.value = True
    print("on")
    time.sleep(1)
    
    pin.value = False
    print("off")
    time.sleep(1)
