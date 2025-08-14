## --- Rotary Encoder (Mouse encoder) --- ##
#     tested with tinkertanks frisbee      #

import time, board, digitalio

rotary_a = digitalio.DigitalInOut(board.GP12)
rotary_a.direction = digitalio.Direction.INPUT
rotary_a.pull = digitalio.Pull.UP

rotary_b = digitalio.DigitalInOut(board.GP13)
rotary_b.direction = digitalio.Direction.INPUT
rotary_b.pull = digitalio.Pull.UP

last_a_state = rotary_a.value
rotation = 0

while True:
    current_a_state = rotary_a.value

    if current_a_state != last_a_state:
        if rotary_b.value != current_a_state:
            rotation += 1  # Clockwise rotation
        else:
            rotation -= 1  # Counter-clockwise rotation
        print("Rotation:", rotation)
        last_a_state = current_a_state
    
    time.sleep(0.01)
