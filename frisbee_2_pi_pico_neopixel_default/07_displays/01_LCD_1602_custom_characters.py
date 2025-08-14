## --------  LED (Digital Output)  ------- ##
#      tested with tinkertanks frisbee      #

# easy use with I2C Backback HW-61

import board, busio
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

i2c = busio.I2C(board.GP21, board.GP20)
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)

# Smiley face bitmap (5x8 pixels)
heart = bytearray([
    0b01010,
    0b11111,
    0b11111,
    0b01110,
    0b00100,
    0b00000,
    0b00000,
    0b00000
])

lcd.create_char(0, heart)

lcd.write(0)

print("!")