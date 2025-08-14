## ---- TINKERTANK MOON ---- ##
## ----- standard code ----- ##

class Keycode:

    A = 0x04
    B = 0x05
    C = 0x06
    D = 0x07
    E = 0x08
    F = 0x09
    G = 0x0A
    H = 0x0B
    I = 0x0C
    J = 0x0D
    K = 0x0E
    L = 0x0F
    M = 0x10
    N = 0x11
    O = 0x12
    P = 0x13
    Q = 0x14
    R = 0x15
    S = 0x16
    T = 0x17
    U = 0x18
    V = 0x19
    W = 0x1A
    X = 0x1B
    Y = 0x1C
    Z = 0x1D

    ONE = 0x1E
    TWO = 0x1F
    THREE = 0x20
    FOUR = 0x21
    FIVE = 0x22
    SIX = 0x23
    SEVEN = 0x24
    EIGHT = 0x25
    NINE = 0x26
    ZERO = 0x27
    ENTER = 0x28
    RETURN = ENTER
    ESCAPE = 0x29
    BACKSPACE = 0x2A
    TAB = 0x2B
    SPACEBAR = 0x2C
    SPACE = SPACEBAR
    MINUS = 0x2D
    EQUALS = 0x2E
    LEFT_BRACKET = 0x2F
    RIGHT_BRACKET = 0x30
    BACKSLASH = 0x31
    POUND = 0x32
    SEMICOLON = 0x33
    QUOTE = 0x34
    GRAVE_ACCENT = 0x35
    COMMA = 0x36
    PERIOD = 0x37
    FORWARD_SLASH = 0x38
    CAPS_LOCK = 0x39

    F1 = 0x3A
    F2 = 0x3B
    F3 = 0x3C
    F4 = 0x3D
    F5 = 0x3E
    F6 = 0x3F
    F7 = 0x40
    F8 = 0x41
    F9 = 0x42
    F10 = 0x43
    F11 = 0x44
    F12 = 0x45

    PRINT_SCREEN = 0x46
    SCROLL_LOCK = 0x47
    PAUSE = 0x48
    INSERT = 0x49
    HOME = 0x4A
    PAGE_UP = 0x4B
    DELETE = 0x4C
    END = 0x4D
    PAGE_DOWN = 0x4E

    RIGHT_ARROW = 0x4F
    LEFT_ARROW = 0x50
    DOWN_ARROW = 0x51
    UP_ARROW = 0x52
    KEYPAD_NUMLOCK = 0x53
    KEYPAD_FORWARD_SLASH = 0x54
    KEYPAD_ASTERISK = 0x55
    KEYPAD_MINUS = 0x56
    KEYPAD_PLUS = 0x57
    KEYPAD_ENTER = 0x58
    KEYPAD_ONE = 0x59
    KEYPAD_TWO = 0x5A
    KEYPAD_THREE = 0x5B
    KEYPAD_FOUR = 0x5C
    KEYPAD_FIVE = 0x5D
    KEYPAD_SIX = 0x5E
    KEYPAD_SEVEN = 0x5F
    KEYPAD_EIGHT = 0x60
    KEYPAD_NINE = 0x61
    KEYPAD_ZERO = 0x62
    KEYPAD_PERIOD = 0x63
    KEYPAD_BACKSLASH = 0x64
    APPLICATION = 0x65
    POWER = 0x66
    KEYPAD_EQUALS = 0x67
    LEFT_CONTROL = 0xE0
    CONTROL = LEFT_CONTROL
    LEFT_SHIFT = 0xE1
    SHIFT = LEFT_SHIFT
    LEFT_ALT = 0xE2
    ALT = LEFT_ALT
    OPTION = ALT
    LEFT_GUI = 0xE3
    GUI = LEFT_GUI
    WINDOWS = GUI
    COMMAND = GUI
    RIGHT_CONTROL = 0xE4
    RIGHT_SHIFT = 0xE5
    RIGHT_ALT = 0xE6
    RIGHT_GUI = 0xE7



## ---- Imports ---- ##
import time
import board
import digitalio
import touchio
import usb_hid
import neopixel
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.mouse import Mouse

## ---- Definitions ---- ##

# ACTIONS (see list above)
actions = [Keycode.UP_ARROW,
           Keycode.LEFT_ARROW,
           Keycode.RIGHT_ARROW,
           Keycode.DOWN_ARROW,
           Mouse.LEFT_BUTTON,
           Keycode.SPACE]

pinValueOld = [0,0,0,0,0,0] # previous pinValues
pinValue = [0,0,0,0,0,0]    # sum of pinValue Readings 
numReadings = 10			# number of readings before evaluating
threshold = 8    			# threshold to trigger key

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
BLUE = (0, 20, 255)
BLACK = (0,0,0)
pxColor = BLACK


# Game controller pins:
input_pin_names = [board.GP10, board.GP11, board.GP12, board.GP13, board.GP20, board.GP21]
input_pins = []

for i in input_pin_names:
    pin = digitalio.DigitalInOut(i)
    pin.direction = digitalio.Direction.INPUT
    input_pins.append(pin)

#set moon pixel pin:
pixels = neopixel.NeoPixel(board.GP14, 1, brightness=1, auto_write=False)

#set touch pin
touch_pad = board.GP6
touch = touchio.TouchIn(touch_pad)
touch.threshold = 2000

# all outer Moon GPIOs to output high #
output_pin_names = [board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP26, board.GP27, board.GP28]
output_pins = []

for i in output_pin_names:
    output_pin = digitalio.DigitalInOut(i)
    output_pin.direction = digitalio.Direction.OUTPUT
    output_pin.value = 1
    output_pins.append(output_pin)

## startup animation
def startup(pc):
    for k in range(80):
        pixels[0] = (k,k*pc,0)
        time.sleep(0.01)
        pixels.show()
        
    pixels[0] = (10,10*pc,0)
    pixels.show()
    time.sleep(0.1)
    pixels[0] = (80,80*pc,0)
    pixels.show()
    time.sleep(0.1)
    pixels[0] = (20,20*pc,0)
    pixels.show()
    time.sleep(0.1)
    pixels[0] = (255,255*pc,0)
    pixels.show()
    time.sleep(1)
    for k in range(0, 255):
        pixels[0] = (255-k,(255-k)*pc,0)
        time.sleep(0.001)
        pixels.show()

try:
    keyboard_HID = Keyboard(usb_hid.devices)
    mouse_HID = Mouse(usb_hid.devices)
except:
    startup(0) #startup animation in yellow (usb computer connection found)
else:
    startup(1) #startup animation in red	(just powered)



## functions ##
    
def evaluatePins():
    global pinValue, pinValueOld, pxColor, actions

    for i in range(6):
        # print (pinValue[i], end=" ")    	# print raw sum values for debugging
        if pinValue[i] > threshold:			# see if average pinValue is higher than threshold
            pinValue[i] = 1
            if i < 4: pxColor = GREEN		# ARROW KEYS: green
            elif i == 4: pxColor = RED      # SPACE: red
            elif i == 5: pxColor = BLUE     # CLICK: blue            
        else:
            pinValue[i] = 0 				# not pressed

        #compare with old state and press or release key
        if pinValueOld[i] < pinValue[i]:
            try:
                if i == 4: mouse_HID.press(Mouse.LEFT_BUTTON)
                else: keyboard_HID.press(actions[i])
            except: p=0
        elif pinValueOld[i] > pinValue[i]:
            try:
                if i == 4: mouse_HID.release(Mouse.LEFT_BUTTON)
                else: keyboard_HID.release(actions[i])
            except: p=0

        pinValueOld[i] = pinValue[i]		# save previous value
        pinValue[i] = 0   					# reset RawValue

## ---- Code ---- ##
while True:
    pxColor = BLACK
 
    for i in range(numReadings):					# read [10] times
        for j in range(6):	   						# read all 6 Game controller Pins
            pinValue[j] += input_pins[j].value		# append to List
        time.sleep(0.002)
    
    evaluatePins()									# check if button pressed
    
    if touch.value:
        pxColor =(YELLOW)
    pixels[0] = pxColor								# moon glowing
    pixels.show()

