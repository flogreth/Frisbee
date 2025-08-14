## ----------- NO DELAYS ----------- ##
#   tested with tinkertanks frisbee   #

import board, time

lastUpdate = 0
interval = 2

while True:
   
    if (time.monotonic()- lastUpdate) > interval:
        lastUpdate = time.monotonic()
        print("action at:", lastUpdate)
        #put your code here
