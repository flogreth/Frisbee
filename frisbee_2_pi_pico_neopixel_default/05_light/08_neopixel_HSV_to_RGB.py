##   ------ NEOPIXEL HSV to RGB ------  ##
#     tested with tinkertanks frisbee    #

import time, board, neopixel, colorsys
num_pixels = 24
pixels = neopixel.NeoPixel(board.GP12 , num_pixels, brightness=0.2, auto_write=False)

while True:
    for i in range(100):
        print(colorsys.hsv_to_rgb(0.5, 1, 0.1))
        
        pixels.fill( colorsys.hsv_to_rgb(0.5, 1, 0.1) )
        pixels.show()
        time.sleep(0.1)
