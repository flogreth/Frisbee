## ---  NEOPIXEL RAINBOW MODES  ---- ##
#    tested with tinkertanks moon     #

import board, neopixel, time

from adafruit_led_animation.animation.rainbow import Rainbow
from adafruit_led_animation.animation.rainbowchase import RainbowChase
from adafruit_led_animation.animation.rainbowcomet import RainbowComet
from adafruit_led_animation.animation.rainbowsparkle import RainbowSparkle
from adafruit_led_animation.animation.blink import Blink
from adafruit_led_animation.animation.chase import Chase

# Update to match the number of NeoPixels you have connected
pixel_num = 15


pins = [board.GP10, board.GP11, board.GP12, board.GP13, board.GP20, board.GP21]
pixels = [neopixel.NeoPixel(pin, pixel_num, brightness=1, auto_write=False) for pin in pins]

chase 		  = Chase(pixels[0], speed=0.02, color=(255,255,0), size=3, spacing=15)
rainbow 	  = Rainbow(	   pixels[1], speed=0.01, period=1)
rainbow_chase = RainbowChase(  pixels[2], speed=0.1, size=3, spacing=5)
rainbow_comet = RainbowComet(  pixels[3], speed=0.05, tail_length=11, bounce=True)
rainbow_spark = RainbowSparkle(pixels[4], speed=0.05, num_sparkles=1)
blink = Blink(  pixels[5], speed=0.5, color=(255,0,0))


while True:
    chase.animate()
    rainbow.animate()
    rainbow_chase.animate()
    rainbow_comet.animate()
    rainbow_spark.animate()
    blink.animate()
    print("running")
    time.sleep(0.01)