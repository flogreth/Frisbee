import board
import neopixel
import time

# NeoPixel an GP26, mit 25 LEDs
pixel_pin = board.GP26
num_pixels = 25

# Farben definieren
RED = (255,0,0)
BLACK = (0,0,0)


# Helligkeit 0.3 = 30%
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=True)

while True:
    pixels.fill(RED)  # Rot
    time.sleep(1)
    pixels.fill(BLACK)  # Grün
    time.sleep(1)
