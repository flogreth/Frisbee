## ----  Time of Flight Distance Sensor VL53L0 ---- ##
#          tested with tinkertanks frisbee           #

import time, board, busio, adafruit_vl53l0x

i2c = busio.I2C(board.GP13, board.GP12)
vl53 = adafruit_vl53l0x.VL53L0X(i2c)

while True:
    print(vl53.range)
    time.sleep(0.02)
