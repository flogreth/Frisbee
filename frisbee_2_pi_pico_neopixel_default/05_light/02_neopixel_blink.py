## ------- NEOPIXEL BLINK ------- ##
#   tested with tinkertanks moon   #

import board, time, neopixel
from adafruit_led_animation.animation.blink import Blink

TEAL = (0,255,120)

pixels = neopixel.NeoPixel(board.GP21, 20, brightness=0.5, auto_write=False)

blink = Blink(pixels, speed=0.2, color=TEAL)

while True:
    blink.animate()