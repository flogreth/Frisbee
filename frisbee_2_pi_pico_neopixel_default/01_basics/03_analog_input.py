## --------  ANALOG INPUT ---------- ##
#   tested with tinkertanks frisbee   #

import board, analogio, time
from adafruit_simplemath import map_range

poti=analogio.AnalogIn(board.GP27) 						# GP26=A0, GP27=A1 , GP28=A2

#SIMPLE:

while True:
    print( int(map_range(poti.value, 0, 2**16, 0, 101)) )		# umrechnung z.B. auf 0 bis 180
    time.sleep(0.1)

# BEISPIELE:

# Umrechnung auf 180° (für Servomotor)
print( int(map_range(poti.value, 0, 2**16, 0, 181)) )

# Umrechnung auf 0-100% 
print( int(map_range(poti.value, 0, 2**16, 0, 101)) )