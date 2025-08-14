class Keycode:
    RIGHT_ARROW = 0x4F
    LEFT_ARROW = 0x50
    DOWN_ARROW = 0x51
    UP_ARROW = 0x52

import time, board, busio, adafruit_mpu6050,usb_hid

i2c = busio.I2C(board.GP13, board.GP12)
mpu = adafruit_mpu6050.MPU6050(i2c)
state = "m"
oldstate = "m"

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.mouse import Mouse



try:
    keyboard_HID = Keyboard(usb_hid.devices)
    mouse_HID = Mouse(usb_hid.devices)
except:
    pass

while True:
    winkel = mpu.acceleration[0]
    
    print(state, winkel)	#single axis
    
    time.sleep(0.05)
    
    if winkel > 8:
        state = "l"
    elif winkel < -8:
        state = "r"
    else:
        state = "m"
    
    
    