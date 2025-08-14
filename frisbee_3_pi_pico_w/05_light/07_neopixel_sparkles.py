## ---  NEOPIXEL SPARKLE MODES  ---- ##
#    tested with tinkertanks moon     #

import board, neopixel, time

from adafruit_led_animation.animation.sparkle import Sparkle
from adafruit_led_animation.animation.sparklepulse import SparklePulse
from adafruit_led_animation.sequence import AnimationSequence
from adafruit_led_animation.color import AMBER, JADE

# Update to match the pin connected to your NeoPixels
pixel_pin = board.GP12
# Update to match the number of NeoPixels you have connected
pixel_num = 25

pixels = neopixel.NeoPixel(pixel_pin, pixel_num, brightness=0.5, auto_write=False)

sparkle = Sparkle(pixels, speed=0.05, color=AMBER, num_sparkles=5)
sparkle_pulse = SparklePulse(pixels, speed=0.01, period=2, color=JADE)

animations = AnimationSequence(
    sparkle,
    sparkle_pulse,
    advance_interval=5,
    auto_clear=True,
)

while True:
    animations.animate()
    print("hi")
    time.sleep(0.05)