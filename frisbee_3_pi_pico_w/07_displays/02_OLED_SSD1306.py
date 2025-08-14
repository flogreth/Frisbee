## ---  OLED DISPLAY SSD1306  --- ##
#   tested with tinkertanks moon   #

import busio,board, time, random
import adafruit_ssd1306

# Create the I2C interface.
i2c = busio.I2C (scl=board.GP21, sda=board.GP20)  #A1(GP27) and A0(GP26) work as well
display = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

display.fill(0) 					# FILL!
display.show()

for j in range(100):
    px = random.randint(0,128)
    py = random.randint(0,50)
    display.pixel(px, py, 1) 		# SINGLE PIXELS!
    display.show()

display.rect(0,52,128,64,1) 		# RECTANGLES!
display.show()

for i in range(4,127,6):
    display.line(i,55,i,60,1) 		# LINES!
    display.show()
    time.sleep(0.1)

for k in range(0,23):
    display.circle(64,24,k,0)		# CIRCLES!
    display.circle(64,24,k+1,1)
    display.show()
    print(k)
    time.sleep(0.02)
    
TT = "TINKER\n TANK"
for X in range(13):
    display.text(TT[:X],47,18,1)   	#TEXT! (in this case letter by letter...)
    display.show()


display.invert(1)
time.sleep(1)
display.invert(0)