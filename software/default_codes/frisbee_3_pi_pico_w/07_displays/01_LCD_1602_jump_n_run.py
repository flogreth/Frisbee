## --------  LED (Digital Output)  ------- ##
#      tested with tinkertanks frisbee      #

# easy use with I2C Backback HW-61

import board, busio, time, random
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

i2c = busio.I2C(board.GP21, board.GP20)
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)

# Smiley face bitmap (5x8 pixels)
walk1 = bytearray([
    0b00110,
    0b00110,
    0b11100,
    0b10110,
    0b01100,
    0b01110,
    0b11010,
    0b10011
])
walk2 = bytearray([
    0b00000,
    0b00110,
    0b00110,
    0b01100,
    0b01111,
    0b01100,
    0b11110,
    0b11100
])

walk3 = bytearray([
    0b00110,
    0b00110,
    0b00100,
    0b01101,
    0b01111,
    0b01110,
    0b11110,
    0b00111
])

obstacle = bytearray([
    0b00100,
    0b00100,
    0b00101,
    0b00101,
    0b10111,
    0b11100,
    0b00100,
    0b00100
])


lcd.clear()
lcd.create_char(0, walk1)
lcd.create_char(1, walk2)
lcd.create_char(2, walk3)
lcd.create_char(3, obstacle)
lcd.write(0)

lastUpdate = 0
walkstate = 1
obstacle_pos = 17
while True:

    if time.monotonic()-lastUpdate > 0.4:
        lastUpdate = time.monotonic()
        lcd.home()
        lcd.clear()
        walkstate = (walkstate+1)%3
        lcd.write(walkstate)
        print(walkstate)
        
        #obstacle
        if obstacle_pos < 16:
            lcd.set_cursor_pos(1, obstacle_pos)
            lcd.write(3)
            
            if obstacle_pos <= 0:
                obstacle_pos = random.randint(17,25)
        obstacle_pos -= 1

print("!")