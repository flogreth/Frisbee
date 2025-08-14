## --------  PWM TÖNE SPIELEN  -------- ##
#    tested with tinkertanks frisbee     #

import board, time, pwmio

frequencies = [
    261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88,   # Oktave 1 (C4 bis H4)
    523.25, 587.33, 659.25, 698.46, 783.99, 880.00, 987.77,   # Oktave 2 (C5 bis H5)
    1046.50, 1174.66, 1318.51, 1396.91, 1567.98, 1760.00, 1975.53  # Oktave 3 (C6 bis H6)
]

speaker = pwmio.PWMOut(board.GP0, duty_cycle=2**15, variable_frequency=True)
speaker.frequency = 400

bpm = 120

def tone(freq, length=1):
    freq = min(len(frequencies),freq)
    speaker.frequency = int(frequencies[freq])
    speaker.duty_cycle = int((2**15))
    time.sleep(length * 60/bpm)
    noTone()

def noTone():
    speaker.duty_cycle = 0


while True:
    tone(0., 0.1)
    time.sleep(0.1)
    
    

