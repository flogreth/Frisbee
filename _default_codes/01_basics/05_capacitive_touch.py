##  ------ CAPACITIVE TOUCH -------  ##
#   tested with tinkertanks frisbee   #

import board, time, touchio

#setup
touch_pad = board.GP12
touch = touchio.TouchIn(touch_pad)
touch.threshold = 5000

while True:
    print("raw value:", touch.raw_value , "/ boolean:", touch.value)
    time.sleep(0.1)
