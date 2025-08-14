## ------- NEOPIXEL CHASE ------- ##
#   tested with tinkertanks moon   #

import board, neopixel 

from adafruit_led_animation.animation.chase import Chase

pixels = neopixel.NeoPixel(board.GP21, 205, brightness=0.5, auto_write=False)

chase = Chase(pixels, speed=0.01, size=3, spacing=16, color=(125,255,0) )

while True:
    chase.animate()

    
