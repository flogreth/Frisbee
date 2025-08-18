##   ------ NEOPIXEL HSV to RGB ------  ##
#     tested with tinkertanks frisbee    #

import time, board, neopixel, colorsys
num_pixels = 1
pixels = neopixel.NeoPixel(board.GP14 , num_pixels, brightness=1, auto_write=False)

while True:
    for hue in range(100):
        pixels.fill( colorsys.hsv_to_rgb(hue*0.01, 1, 0.5) )
        pixels.show()
        #print(hue/100)
        time.sleep(0.08)
