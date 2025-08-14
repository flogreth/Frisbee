## ---  NEOPIXEL COLORCYLCE  ---- ##
#   tested with tinkertanks moon   #

import board, time, neopixel
import adafruit_led_animation as ani

from adafruit_led_animation.animation.colorcycle import ColorCycle
from adafruit_led_animation.color import MAGENTA, ORANGE, TEAL, RED

pixels = neopixel.NeoPixel(board.GP12, 25, brightness=0.7, auto_write=False)

colorcycle = ColorCycle(pixels, 0.2, colors=[MAGENTA, ORANGE, TEAL])

while True:
    colorcycle.animate()