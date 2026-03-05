## --------  PWM TÖNE SPIELEN  -------- ##
#    tested with tinkertanks frisbee     #

import board, neopixel, time

# NeoPixel an GP26, mit 25 LEDs
pixel_pin = board.GP12
numpixels = 30

# Farben definieren
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)

pixels = neopixel.NeoPixel(pixel_pin, numpixels, brightness=0.8, auto_write=True)	# Helligkeit 0.8 = 80%

while True:
    pixels.fill(RED)  # alle auf einmal rot
    time.sleep(1)
    pixels.fill(BLACK)  # alle auf einmal schwarz
    time.sleep(1)
    
    #nacheinander einzeln alle pixel grün:
    for i in range (numpixels):
        pixels[i] = GREEN = (0,255,0)
        pixels.show()
        time.sleep(0.03)
