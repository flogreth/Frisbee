import board
import neopixel
import time

# NeoPixel an GP12, mit nur 1 LED
pixel_pin = board.GP26
num_pixels = 25

# Helligkeit 0.3 = 30%
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=True)

while True:
    pixels.fill((255, 0, 0))  # Rot
    time.sleep(1)
    pixels.fill((0, 0, 0))  # Grün
    time.sleep(1)
