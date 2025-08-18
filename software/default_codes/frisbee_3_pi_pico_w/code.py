##   ------ NEOPIXEL HSV to RGB ------  ##
#     tested with tinkertanks frisbee    #

import time, board, neopixel, colorsys, touchio
num_pixels = 1
pixels = neopixel.NeoPixel(board.GP14 , num_pixels, brightness=1, auto_write=False)

#touch
touch = touchio.TouchIn(board.GP6)
touch.threshold = 2000

hue = 0

while True:
    if touch.value:
        print(hue)
        hue += 0.01

    pixels.fill( colorsys.hsv_to_rgb(hue, 1, 0.5) )
    pixels.show()
    time.sleep(0.02)
        
