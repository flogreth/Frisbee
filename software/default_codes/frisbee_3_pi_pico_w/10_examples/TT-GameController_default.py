## ---- TINKERTANK FRISBEE ---- ##
## ------ standard code ------- ##

from keys import Keycode  # deine ausgelagerte Keycode-Klasse
import time
import board
import digitalio
import touchio
import usb_hid
import neopixel
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.mouse import Mouse

## ---- Konfiguration ---- ##
# Reihenfolge: [UP, LEFT, RIGHT, DOWN, SPACE, CLICK ] 
Pins = [10, 11, 12, 13, 21, 20]

# Möglichkeiten: "MOUSE_LEFT", UP_ARROW, A, B, C, ONE, TWO, THREE, ...
KeyMappings = [
    Keycode.TWO,
    Keycode.ONE,
    Keycode.THREE,
    Keycode.FOUR,
    None,
    None  
]
LED_PIN = 14
TOUCH_PIN = 16

## ---- Farbdefinitionen ---- ##
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
BLUE = (0, 20, 255)
BLACK = (0, 0, 0)

## ---- Parameter ---- ##
numReadings = 10
threshold = 8
pxColor = BLACK
pinValue = [0] * len(Pins)
pinValueOld = [0] * len(Pins)

## ---- Setup ---- ##

# Eingabepins automatisch erstellen
InputPins = []
for p in Pins:
    pin = digitalio.DigitalInOut(getattr(board, f"GP{p}"))
    pin.direction = digitalio.Direction.INPUT
    InputPins.append(pin)

# LED
pixels = neopixel.NeoPixel(getattr(board, f"GP{LED_PIN}"), 1, brightness=1, auto_write=False)

# Touch
touch_pad = getattr(board, f"GP{TOUCH_PIN}")
touch = touchio.TouchIn(touch_pad)
touch.threshold = 2000

# Alle übrigen Pins auf HIGH setzen (gegen Störungen)
for i in [0, 1, 2, 3, 4, 5, 26, 27, 28]:
    highPin = digitalio.DigitalInOut(getattr(board, f"GP{i}"))
    highPin.direction = digitalio.Direction.OUTPUT
    highPin.value = True


## ---- Startup Animation ---- ##
def startup(pc):
    for k in range(80):
        pixels[0] = (k, k * pc, 0)
        time.sleep(0.01)
        pixels.show()

    pixels[0] = (255, 255 * pc, 0)
    pixels.show()
    time.sleep(1)
    for k in range(255):
        pixels[0] = (255 - k, (255 - k) * pc, 0)
        pixels.show()
        time.sleep(0.001)


try:
    keyboard_HID = Keyboard(usb_hid.devices)
    mouse_HID = Mouse(usb_hid.devices)
except Exception:
    startup(0)  # gelb
else:
    startup(1)  # rot


## ---- Funktionen ---- ##
def sensePin(pinIndex):
    """Addiere aktuellen Pinwert auf Summe"""
    global pinValue
    pinValue[pinIndex] += InputPins[pinIndex].value


def evaluatePins():
    """Überprüfe Pins und löse Key- oder Maus-Events aus"""
    global pinValue, pinValueOld, pxColor
    pxColor = BLACK

    for i in range(len(Pins)):
        pressed = pinValue[i] > threshold
        pinValue[i] = 1 if pressed else 0

        # LED-Farbe pro Taste
        if pressed:
            if i < 4:
                pxColor = GREEN
            elif i == 4:
                pxColor = RED
            elif i == 5:
                pxColor = BLUE

        # Tastendruck erkannt
        if pinValueOld[i] < pinValue[i]:
            try:
                mapping = KeyMappings[i]
                if mapping is None:
                    continue
                if mapping == "MOUSE_LEFT":
                    mouse_HID.press(Mouse.LEFT_BUTTON)
                else:
                    keyboard_HID.press(mapping)
            except Exception:
                pass

        # Taste losgelassen
        elif pinValueOld[i] > pinValue[i]:
            try:
                mapping = KeyMappings[i]
                if mapping == "MOUSE_LEFT":
                    mouse_HID.release(Mouse.LEFT_BUTTON)
                else:
                    keyboard_HID.release(mapping)
            except Exception:
                pass

        pinValueOld[i] = pinValue[i]
        pinValue[i] = 0


def readTouchPoint():
    global touch, pxColor
    if touch.value:
        pxColor = YELLOW


## ---- Hauptschleife ---- ##
while True:
    pxColor = BLACK

    for i in range(numReadings):
        for j in range(len(Pins)):
            sensePin(j)
        time.sleep(0.002)

    evaluatePins()
    readTouchPoint()

    pixels[0] = pxColor
    pixels.show()
