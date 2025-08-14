## ----  Lagesensor MPU6050 (gy-521) ---- ##
#     tested with tinkertanks frisbee      #

import time, board, busio, adafruit_mpu6050, neopixel

i2c = busio.I2C(board.GP13, board.GP12)
mpu = adafruit_mpu6050.MPU6050(i2c)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0,0,0)
numpixels = 200
pixels = neopixel.NeoPixel(board.GP14, numpixels, brightness=1, auto_write=False) #z.B. 1 Pixel an pin GP14 (der Mond)

while True:
    print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2" % (mpu.acceleration))
    print("Gyro X:%.2f, Y: %.2f, Z: %.2f rad/s" % (mpu.gyro))
    print("Temperature: %.2f C" % mpu.temperature)
    
    print(mpu.gyro[2])	#single axis
    
    time.sleep(0.1)
    
    