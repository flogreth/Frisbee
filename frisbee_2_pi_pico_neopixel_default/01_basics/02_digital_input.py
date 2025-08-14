## ----  DIGITAL INPUT (button) ---- ##
#   tested with tinkertanks frisbee   #

import time, board, digitalio

button = digitalio.DigitalInOut(board.GP12)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.DOWN

# simple Usage: #

while True: 
    print(button.value)
    time.sleep(0.1)


# Advanced Usage: #
old_state = button.value
while True:
    cur_state = button.value
    if cur_state < old_state:
            print("Button down")
    elif cur_state > old_state:
            print("Button up")
    old_state = cur_state