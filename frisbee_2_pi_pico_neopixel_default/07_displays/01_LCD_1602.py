## --------  LED (Digital Output)  ------- ##
#      tested with tinkertanks frisbee      #

# easy use with I2C Backback HW-61

import board, busio
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

i2c = busio.I2C(board.GP21, board.GP20)
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)

lcd.clear()
lcd.set_cursor_pos(0, 3)
lcd.print("TINKERTANK")

# other commands:
lcd.shift_display(0)
lcd.set_backlight(1)

