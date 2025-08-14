import time, board, busio, adafruit_mpu6050, neopixel
#from bmp_reader import BMPReader

#img = BMPReader('image.bmp')
current_col = 0

pixels = neopixel.NeoPixel(board.GP6, img.height, brightness=1, auto_write=False) #number of pixels depending on bmp size

pixel_grid = img.get_pixels()
i = 0

i2c = busio.I2C(board.GP21, board.GP20)
mpu = adafruit_mpu6050.MPU6050(i2c)

lastAccelUpdate, lastPixelUpdate, lastTurn, direction, wiggle_freq = 0, 0, 0, 1, 0  
lastAccelData = [0] * 3 	# raw accel data smoothing is 3 values 
smoothedAccel = [0] * 2 	# last 2 accel datapoints
peak_timestamp = [0] * 4 	# consider last 4 peaks



def calc_avg_time():
    wiggle_freq = sum(peak_timestamp) / len(peak_timestamp)

while True:
    if time.monotonic()-lastAccelUpdate > 0.005:
        print("X-Acceleration: %.2f" % (mpu.acceleration[0]))
        
        # smooth accel data
        lastAccelData.append(mpu.acceleration[0])
        lastAccelData.pop(0)
        
        # add to 
        smoothedAccel.append( sum(lastAccelData) / len(lastAccelData) )
        smoothedAccel.pop(0)
        
        # get the peak times
        if smoothedAccel[0] > smoothedAccel[1] and direction == 1:
            peak_timestamp.append (time.monotonic() - peak_timestamp[-1])
            peak_timestamp.pop(0)
            direction = -1
            calc_avg_time()
            print("-->")
            
        if smoothedAccel[0] < smoothedAccel[1] and direction == -1:
            peak_timestamp.append (time.monotonic() - peak_timestamp[-1])
            peak_timestamp.pop(0)
            direction = 1
            calc_avg_time()
            print("<--")
    
    if time.monotonic()-lastTurn > wiggle_freq:
        lastTurn = time.monotonic()
        
        

    if time.monotonic()- lastPixelUpdate > (wiggle_freq/img.width):
        lastPixelUpdate = time.monotonic()
        
        #for row in range(img.height):
            #pixels[row] = pixel_grid[row][current_col]

        #pixels.show()
        #current_col += direction #add 1 or -1 to current column
        