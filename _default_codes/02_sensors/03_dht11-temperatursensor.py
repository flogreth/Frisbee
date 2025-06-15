## ----  Temperatursensor & Feuchtigkeit DHT-11 ---- ##
#           tested with tinkertanks frisbee           #

import time, adafruit_dht, board

dht = adafruit_dht.DHT11(board.GP12)

while True:
    try:
        print("Temperature:", dht.temperature, "  Humidity:", dht.humidity)        
    
    except RuntimeError as e:
        print("Reading from DHT failure: ", e.args)

    time.sleep(1)
    

# DHT11 PINOUT:

    ###
    ###
    ###
#   |||
#  D - +