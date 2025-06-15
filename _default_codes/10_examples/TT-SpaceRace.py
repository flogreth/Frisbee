## -------  SPACE RACE -------- ##

import board, analogio,time, neopixel, pwmio, adafruit_ssd1306, busio,os
from adafruit_simplemath import map_range
from adafruit_simplemath import constrain
from adafruit_led_animation.animation.rainbow import Rainbow

# Create the I2C interface.
i2c = busio.I2C (scl=board.GP21, sda=board.GP20)  #A1(GP27) and A0(GP26) work as well
display = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)
bestLap = 999.999

try:
    file=open('best.txt','r')
    readvalue = file.readline()
    bestLap= float(readvalue)
    file.close()
except:
    pass


try:
    file=open('best.txt','w')
    file.write(str(bestLap))
    file.close()
    display.text("Highscore loaded",0,5,1)
    display.show()
except:
    display.text("loading failed..",10,5,1)
    display.show()
######
time.sleep(2)

display.fill(0)
display.text("BEST LAP:" + str(bestLap) + "s",0,5,1)
display.show()




speaker = pwmio.PWMOut(board.GP0, duty_cycle=2**15, variable_frequency=True)	# speaker on pin 0

numpixels = 188
pixels = neopixel.NeoPixel(board.GP1, numpixels, brightness=1, auto_write=False) #z.B. 1 Pixel an pin GP14 (der Mond)
planets = neopixel.NeoPixel(board.GP12, 25, brightness=1, auto_write=False)
rainbow = Rainbow(planets, speed=0.01, period=1)


analogA1=analogio.AnalogIn(board.GP27) #A1 
analogA0=analogio.AnalogIn(board.GP26)	#A0

lastLap = 999.99
lastStep = time.monotonic()
lastUpdate = time.monotonic()
lastLapUpdate = time.monotonic()
speed = 0
position = 0
penalty = 0
speedstep = 0
threshold = [100,100,100,100,100,100,100,100,100,100,100,100,100,100,60,60,60,60,60,60,
             100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,50,40,
             40,50,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,90,90,
             100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,
             30,30,30,
             100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,80,40,50,40,40,40,60,60,60,70,80,100,100,100,100,100,100,100,
             90,80,75,75,77,79,85,100,100,100,100,100,100,100,80,80,80,78,75,78,80,85,85,85,85,87,89,95,
             100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,
             90,90,80,80,80,80,80,80,75,75,80,100,100,100,100,100,100,100,100,100,100,100,100,100,100]

#for i in range(numpixels):
#    pixels[i] = (255-threshold[i]*2.55, threshold[i]*2.55, 0)
#    pixels.show()     
#time.sleep(5)


def penalty():
    global speed
    for i in range(4):
        speaker.frequency = 80
        pixels[position] = (0, 0, 0)
        pixels.show()
        time.sleep(0.1)
        speaker.frequency = 1
        pixels[position] = (255, 0, 0)
        pixels.show()
        time.sleep(0.1)
    speed = 0

while True:
    rainbow.animate()
    throttle = map_range(analogA1.value, 42000, 14000, 0,100)
    breaks = map_range(analogA0.value, 17600, 45000, 0, 100)
    # Print the values
    # 
    # Wait a bit before reading again
    
    time.sleep(0.001)

    if time.monotonic()-lastUpdate > 0.01:
        lastUpdate = time.monotonic()
        
        speed += ((throttle/90) -0.5 )-(breaks/120)
        speed = constrain(speed, 0,100)
        speedstep = 5/(speed*1.5+0.001)
        
        if speed > 1:
            if (time.monotonic() - lastStep) > speedstep:
                pixels[position] = (0, 0, 0)
                position = (position +1 ) % numpixels
                pixels[position] = (0, 0, 255)
                pixels.show()
                lastStep = time.monotonic()
                
                if threshold[position] < speed:
                    penalty()
                
                # LAP
                
                if position == numpixels-1:
                    lastLap = time.monotonic()-lastLapUpdate
                    lastLapUpdate = time.monotonic()
                    
                    #best lap?
                    if lastLap < bestLap:
                        try:
                            file=open('best/best.txt','w')
                            file.write(str(lastLap))
                            file.close()
                            pixels.fill((0,255,0))
                        except:
                            pixels.fill((255,0,0))
                            #
                        pixels.show()
                        time.sleep(0.1)
                        pixels.fill((0,0,0))
                        pixels.show()
                        bestLap = lastLap

                    display.fill(0) 					# FILL!             
                    display.text("BEST LAP:" + str(bestLap) + "s",0,18,1)
                    display.text("LAST LAP:" + str(lastLap) + "s",0,38,1)
                    display.show()

        speaker.frequency = int(map_range(speed, 0,100, 8,320))
        
        if (threshold[position] - speed ) < 20:
            speaker.frequency = 5000
        #print("Trottle:", throttle, "\t   Breaks:", breaks)
        #print("\t   SPEED:", speed, "\t   speedstep:", speedstep)


