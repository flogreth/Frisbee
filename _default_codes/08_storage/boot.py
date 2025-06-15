# SPDX-FileCopyrightText: 2017 Limor Fried for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials Storage logging boot.py file"""
import board
import digitalio
import storage, neopixel

pixels = neopixel.NeoPixel(board.GP14, 1, brightness=1, auto_write=False) #z.B. 1 Pixel an pin GP14 (der Mond)

switch = digitalio.DigitalInOut(board.GP2)
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.UP

# If the switch pin is connected to ground CircuitPython can write to the drive
storage.remount("/", switch.value)

# bee/moon color:
pixels.fill((255*switch.value, 255-(255*switch.value), 0))
pixels.show()
