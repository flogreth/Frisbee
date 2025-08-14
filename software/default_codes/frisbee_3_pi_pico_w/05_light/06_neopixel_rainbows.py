## ---  NEOPIXEL RAINBOW MODES  ---- ##
#    tested with tinkertanks moon     #

import board, neopixel
import adafruit_fancyled.adafruit_fancyled as fancy
from adafruit_led_animation.animation.rainbow import Rainbow
from adafruit_led_animation.animation.rainbowchase import RainbowChase
from adafruit_led_animation.animation.rainbowcomet import RainbowComet
from adafruit_led_animation.animation.rainbowsparkle import RainbowSparkle
from adafruit_led_animation.sequence import AnimationSequence

# Update to match the pin connected to your NeoPixels
pixel_pin = board.GP13
# Update to match the number of NeoPixels you have connected
pixel_num = 256

pixels = neopixel.NeoPixel(pixel_pin, pixel_num, brightness=0.5, auto_write=False)

rainbow = Rainbow(pixels, speed=0.01, period=1)
rainbow_chase = RainbowChase(pixels, speed=0.1, size=5, spacing=3)
rainbow_comet = RainbowComet(pixels, speed=0.05, tail_length=11, bounce=True)
rainbow_sparkle = RainbowSparkle(pixels, speed=0.1, num_sparkles=15)


animations = AnimationSequence(
    rainbow,
    rainbow_chase,
    rainbow_comet,
    rainbow_sparkle,
    advance_interval=5,
    auto_clear=True,
)

while True:
    animations.animate()