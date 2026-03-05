##   ------ TINKERTANK FRISBEE ------  ##

import board, time, neopixel, touchio

touch_pad = board.GP6
touch = touchio.TouchIn(touch_pad)
touch.threshold = 5000

# Farben definieren
BLACK = (0,0,0)
GREEN = (0,255,0)

bee = neopixel.NeoPixel(board.GP14, 1, brightness=1, auto_write=True)	# Helligkeit 0.8 = 80%

while True:
    print("Diese Frisbee läuft seit",time.monotonic(),"Sekunden und wartet darauf, programmiert zu werden :-)")
    time.sleep(0.05)
    
    if touch.value:
        bee.fill(GREEN)
    else:
        bee.fill(BLACK)
        
        
        