## ---- TINKERTANK FRISBEE ---- ##
## ------ standard code ------- ##

class Keycode:

# pylint: disable-msg=invalid-name

    A = 0x04
    """``a`` and ``A``"""
    B = 0x05
    """``b`` and ``B``"""
    C = 0x06
    """``c`` and ``C``"""
    D = 0x07
    """``d`` and ``D``"""
    E = 0x08
    """``e`` and ``E``"""
    F = 0x09
    """``f`` and ``F``"""
    G = 0x0A
    """``g`` and ``G``"""
    H = 0x0B
    """``h`` and ``H``"""
    I = 0x0C
    """``i`` and ``I``"""
    J = 0x0D
    """``j`` and ``J``"""
    K = 0x0E
    """``k`` and ``K``"""
    L = 0x0F
    """``l`` and ``L``"""
    M = 0x10
    """``m`` and ``M``"""
    N = 0x11
    """``n`` and ``N``"""
    O = 0x12
    """``o`` and ``O``"""
    P = 0x13
    """``p`` and ``P``"""
    Q = 0x14
    """``q`` and ``Q``"""
    R = 0x15
    """``r`` and ``R``"""
    S = 0x16
    """``s`` and ``S``"""
    T = 0x17
    """``t`` and ``T``"""
    U = 0x18
    """``u`` and ``U``"""
    V = 0x19
    """``v`` and ``V``"""
    W = 0x1A
    """``w`` and ``W``"""
    X = 0x1B
    """``x`` and ``X``"""
    Y = 0x1C
    """``y`` and ``Y``"""
    Z = 0x1D
    """``z`` and ``Z``"""

    ONE = 0x1E
    """``1`` and ``!``"""
    TWO = 0x1F
    """``2`` and ``@``"""
    THREE = 0x20
    """``3`` and ``#``"""
    FOUR = 0x21
    """``4`` and ``$``"""
    FIVE = 0x22
    """``5`` and ``%``"""
    SIX = 0x23
    """``6`` and ``^``"""
    SEVEN = 0x24
    """``7`` and ``&``"""
    EIGHT = 0x25
    """``8`` and ``*``"""
    NINE = 0x26
    """``9`` and ``(``"""
    ZERO = 0x27
    """``0`` and ``)``"""
    ENTER = 0x28
    """Enter (Return)"""
    RETURN = ENTER
    """Alias for ``ENTER``"""
    ESCAPE = 0x29
    """Escape"""
    BACKSPACE = 0x2A
    """Delete backward (Backspace)"""
    TAB = 0x2B
    """Tab and Backtab"""
    SPACEBAR = 0x2C
    """Spacebar"""
    SPACE = SPACEBAR
    """Alias for SPACEBAR"""
    MINUS = 0x2D
    """``-` and ``_``"""
    EQUALS = 0x2E
    """``=` and ``+``"""
    LEFT_BRACKET = 0x2F
    """``[`` and ``{``"""
    RIGHT_BRACKET = 0x30
    """``]`` and ``}``"""
    BACKSLASH = 0x31
    r"""``\`` and ``|``"""
    POUND = 0x32
    """``#`` and ``~`` (Non-US keyboard)"""
    SEMICOLON = 0x33
    """``;`` and ``:``"""
    QUOTE = 0x34
    """``'`` and ``"``"""
    GRAVE_ACCENT = 0x35
    r""":literal:`\`` and ``~``"""
    COMMA = 0x36
    """``,`` and ``<``"""
    PERIOD = 0x37
    """``.`` and ``>``"""
    FORWARD_SLASH = 0x38
    """``/`` and ``?``"""

    CAPS_LOCK = 0x39
    """Caps Lock"""

    F1 = 0x3A
    """Function key F1"""
    F2 = 0x3B
    """Function key F2"""
    F3 = 0x3C
    """Function key F3"""
    F4 = 0x3D
    """Function key F4"""
    F5 = 0x3E
    """Function key F5"""
    F6 = 0x3F
    """Function key F6"""
    F7 = 0x40
    """Function key F7"""
    F8 = 0x41
    """Function key F8"""
    F9 = 0x42
    """Function key F9"""
    F10 = 0x43
    """Function key F10"""
    F11 = 0x44
    """Function key F11"""
    F12 = 0x45
    """Function key F12"""

    PRINT_SCREEN = 0x46
    """Print Screen (SysRq)"""
    SCROLL_LOCK = 0x47
    """Scroll Lock"""
    PAUSE = 0x48
    """Pause (Break)"""

    INSERT = 0x49
    """Insert"""
    HOME = 0x4A
    """Home (often moves to beginning of line)"""
    PAGE_UP = 0x4B
    """Go back one page"""
    DELETE = 0x4C
    """Delete forward"""
    END = 0x4D
    """End (often moves to end of line)"""
    PAGE_DOWN = 0x4E
    """Go forward one page"""

    RIGHT_ARROW = 0x4F
    """Move the cursor right"""
    LEFT_ARROW = 0x50
    """Move the cursor left"""
    DOWN_ARROW = 0x51
    """Move the cursor down"""
    UP_ARROW = 0x52
    """Move the cursor up"""

    KEYPAD_NUMLOCK = 0x53
    """Num Lock (Clear on Mac)"""
    KEYPAD_FORWARD_SLASH = 0x54
    """Keypad ``/``"""
    KEYPAD_ASTERISK = 0x55
    """Keypad ``*``"""
    KEYPAD_MINUS = 0x56
    """Keyapd ``-``"""
    KEYPAD_PLUS = 0x57
    """Keypad ``+``"""
    KEYPAD_ENTER = 0x58
    """Keypad Enter"""
    KEYPAD_ONE = 0x59
    """Keypad ``1`` and End"""
    KEYPAD_TWO = 0x5A
    """Keypad ``2`` and Down Arrow"""
    KEYPAD_THREE = 0x5B
    """Keypad ``3`` and PgDn"""
    KEYPAD_FOUR = 0x5C
    """Keypad ``4`` and Left Arrow"""
    KEYPAD_FIVE = 0x5D
    """Keypad ``5``"""
    KEYPAD_SIX = 0x5E
    """Keypad ``6`` and Right Arrow"""
    KEYPAD_SEVEN = 0x5F
    """Keypad ``7`` and Home"""
    KEYPAD_EIGHT = 0x60
    """Keypad ``8`` and Up Arrow"""
    KEYPAD_NINE = 0x61
    """Keypad ``9`` and PgUp"""
    KEYPAD_ZERO = 0x62
    """Keypad ``0`` and Ins"""
    KEYPAD_PERIOD = 0x63
    """Keypad ``.`` and Del"""
    KEYPAD_BACKSLASH = 0x64
    """Keypad ``\\`` and ``|`` (Non-US)"""

    APPLICATION = 0x65
    """Application: also known as the Menu key (Windows)"""
    POWER = 0x66
    """Power (Mac)"""
    KEYPAD_EQUALS = 0x67
    """Keypad ``=`` (Mac)"""
    F13 = 0x68
    """Function key F13 (Mac)"""
    F14 = 0x69
    """Function key F14 (Mac)"""
    F15 = 0x6A
    """Function key F15 (Mac)"""
    F16 = 0x6B
    """Function key F16 (Mac)"""
    F17 = 0x6C
    """Function key F17 (Mac)"""
    F18 = 0x6D
    """Function key F18 (Mac)"""
    F19 = 0x6E
    """Function key F19 (Mac)"""

    F20 = 0x6F
    """Function key F20"""
    F21 = 0x70
    """Function key F21"""
    F22 = 0x71
    """Function key F22"""
    F23 = 0x72
    """Function key F23"""
    F24 = 0x73
    """Function key F24"""

    LEFT_CONTROL = 0xE0
    """Control modifier left of the spacebar"""
    CONTROL = LEFT_CONTROL
    """Alias for LEFT_CONTROL"""
    LEFT_SHIFT = 0xE1
    """Shift modifier left of the spacebar"""
    SHIFT = LEFT_SHIFT
    """Alias for LEFT_SHIFT"""
    LEFT_ALT = 0xE2
    """Alt modifier left of the spacebar"""
    ALT = LEFT_ALT
    """Alias for LEFT_ALT; Alt is also known as Option (Mac)"""
    OPTION = ALT
    """Labeled as Option on some Mac keyboards"""
    LEFT_GUI = 0xE3
    """GUI modifier left of the spacebar"""
    GUI = LEFT_GUI
    """Alias for LEFT_GUI; GUI is also known as the Windows key, Command (Mac), or Meta"""
    WINDOWS = GUI
    """Labeled with a Windows logo on Windows keyboards"""
    COMMAND = GUI
    """Labeled as Command on Mac keyboards, with a clover glyph"""
    RIGHT_CONTROL = 0xE4
    """Control modifier right of the spacebar"""
    RIGHT_SHIFT = 0xE5
    """Shift modifier right of the spacebar"""
    RIGHT_ALT = 0xE6
    """Alt modifier right of the spacebar"""
    RIGHT_GUI = 0xE7
    """GUI modifier right of the spacebar"""

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

Pin10= digitalio.DigitalInOut(board.GP10)
Pin10.direction=digitalio.Direction.INPUT

Pin11= digitalio.DigitalInOut(board.GP11)
Pin11.direction=digitalio.Direction.INPUT

Pin12= digitalio.DigitalInOut(board.GP12)
Pin12.direction=digitalio.Direction.INPUT

Pin13= digitalio.DigitalInOut(board.GP13)
Pin13.direction=digitalio.Direction.INPUT

Pin20= digitalio.DigitalInOut(board.GP20)
Pin20.direction=digitalio.Direction.INPUT

Pin21= digitalio.DigitalInOut(board.GP21)
Pin21.direction=digitalio.Direction.INPUT

pixels = neopixel.NeoPixel(board.GP14, 1, brightness=1, auto_write=False)



#touch
touch_pad = board.GP6
touch = touchio.TouchIn(touch_pad)
touch.threshold = 2000

# all GPIOs to output high #
 highPin0= digitalio.DigitalInOut(board.GP0)
highPin0.direction=digitalio.Direction.OUTPUT
highPin0.value = 1

highPin1= digitalio.DigitalInOut(board.GP1)
highPin1.direction=digitalio.Direction.OUTPUT
highPin1.value = 1

highPin2= digitalio.DigitalInOut(board.GP2)
highPin2.direction=digitalio.Direction.OUTPUT
highPin2.value = 1

highPin3= digitalio.DigitalInOut(board.GP3)
highPin3.direction=digitalio.Direction.OUTPUT
highPin3.value = 1

highPin4= digitalio.DigitalInOut(board.GP4)
highPin4.direction=digitalio.Direction.OUTPUT
highPin4.value = 1    
            
highPin5= digitalio.DigitalInOut(board.GP5)
highPin5.direction=digitalio.Direction.OUTPUT
highPin5.value = 1

highPin26= digitalio.DigitalInOut(board.GP26)
highPin26.direction=digitalio.Direction.OUTPUT
highPin26.value = 1

highPin27= digitalio.DigitalInOut(board.GP27)
highPin27.direction=digitalio.Direction.OUTPUT
highPin27.value = 1

highPin28= digitalio.DigitalInOut(board.GP28)
highPin28.direction=digitalio.Direction.OUTPUT
highPin28.value = 1

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
    startup(0) #startup animation in yellow
else:
    startup(1) #startup animation in red



## functions ##

def sensePin(pin):    # digital Read pins and add to 'pinValue' variable
    global pinValue  
    if pin == 0:                      
        pinValue[0] += Pin10.value
    elif pin == 1:
        pinValue[1] += Pin11.value
    elif pin == 2:
        pinValue[2] += Pin12.value
    elif pin == 3:
        pinValue[3] += Pin13.value
    elif pin == 4:
        pinValue[4] += Pin20.value
    elif pin == 5:
        pinValue[5] += Pin21.value

def evaluatePins():             # evaluate 'pinValue'
    for i in range(6):
        global pinValue, pinValueOld, pxColor 
        
        # print (pinValue[i], end=" ")    	# print raw sum values for debugging
        if pinValue[i] > threshold:			# see if pinValue is higher than threshold
            pinValue[i] = 1
            if i < 4: pxColor = GREEN		#arrow keys: green
            elif i == 4: pxColor = RED
            elif i == 5: pxColor = BLUE
            
        else:
            pinValue[i] = 0 # not pressed
            
        if pinValueOld[i] < pinValue[i]:
            try:
                if i == 0: keyboard_HID.press(Keycode.LEFT_ARROW)
                elif i == 1: keyboard_HID.press(Keycode.UP_ARROW)
                elif i == 2: keyboard_HID.press(Keycode.DOWN_ARROW)
                elif i == 3: keyboard_HID.press(Keycode.RIGHT_ARROW)
                elif i == 4: mouse_HID.press(Mouse.LEFT_BUTTON)
                elif i == 5: keyboard_HID.press(Keycode.SPACE)
            except:
                p = 0
            else:
                p = 0
        elif pinValueOld[i] > pinValue[i]:
            try:
                if i == 0: keyboard_HID.release(Keycode.UP_ARROW)
                elif i == 1: keyboard_HID.release(Keycode.LEFT_ARROW)
                elif i == 2: keyboard_HID.release(Keycode.DOWN_ARROW)
                elif i == 3: keyboard_HID.release(Keycode.RIGHT_ARROW)
                elif i == 4: mouse_HID.release(Mouse.LEFT_BUTTON)
                elif i == 5: keyboard_HID.release(Keycode.SPACE)
            except:
                p = 0
            else:
                p = 0
        pinValueOld[i] = pinValue[i]		# save previous value
        pinValue[i] = 0   					# reset RawValue
    
def readTouchPoint():
    global touch, pxColor
    if touch.value:
        pxColor =(YELLOW)



## ---- Code ---- ##
while True:
    pxColor = BLACK
 
    for i in range(numReadings):	#read [10] times
        for j in range(6):	
            sensePin(j)		# read all 6 Pins
        time.sleep(0.002)

    evaluatePins()
    readTouchPoint()
    print(touch.raw_value)

    pixels[0] = pxColor
    pixels.show()
    
    # print('')   #for debugging






