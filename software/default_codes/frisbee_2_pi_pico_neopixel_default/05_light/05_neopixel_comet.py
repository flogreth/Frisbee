## ------- NEOPIXEL COMET ------- ##
#   tested with tinkertanks moon   #

import board, neopixel

from adafruit_led_animation.animation.comet import Comet

pixels = neopixel.NeoPixel(board.GP12, 25, brightness=0.5, auto_write=False)

comet = Comet(pixels, speed=0.03, color=(0,0,255), tail_length=17, bounce=True)

while True:
    comet.animate()