import board, time, touchio, pwmio, math, analogio, neopixel, audiocore, audiopwmio, digitalio

speed = 0.26
takte = 16
steps = 4
last_tick = 0
takt = 0
synthie = []
drums = []

COLOR = [(5,0,0), (255, 0, 0), (0, 255, 0),(0, 0, 255), (255,255,255), (255, 255, 0), (255, 0, 255)]

klaviatur = [0, 523, 493, 587, 349, 392, 440]

for i in range(takte*steps):
    synthie.append(0)
for i in range(takte):
    drums.append(0)

def map_value(value, in_min, in_max, out_min, out_max):
    return int((value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

#setup
analog_in = analogio.AnalogIn(board.GP26)
analog_in2 = analogio.AnalogIn(board.GP27)
speaker = pwmio.PWMOut(board.GP0, duty_cycle=2**15, variable_frequency=True)
speaker2 = digitalio.DigitalInOut(board.GP1)
speaker2.direction = digitalio.Direction.OUTPUT

pins = [board.GP10, board.GP11, board.GP12, board.GP13, board.GP20, board.GP21]
touch_inputs = [touchio.TouchIn(pin) for pin in pins]
drum_switch = touchio.TouchIn(board.GP6)
pixels = neopixel.NeoPixel(board.GP14, 1, brightness=1, auto_write=False)

while True:
    if time.monotonic() - last_tick > speed/steps:
        #print(takt)
        takt = (takt+1) % (takte*steps)
        last_tick = time.monotonic()

    #drums
        if takt % steps == 0:
            pixels[0] = COLOR[synthie[takt]] 			#PIXEL COLOR
            pixels.show()
            speaker2.value=1
            time.sleep(0.01)
            speaker2.value=0
        
        
    if time.monotonic() - last_tick > (speed/steps)/3: 		#PIXEL OFF
        pixels[0] = (0,0,0)
        pixels.show()
        

# INPUT SYNTHIE & DRUMS
    for i in range(6):
        if touch_inputs[i].value == True:
            if drum_switch.value == False:
                synthie[takt] = i+1				# TON
            else:
                drums[takt] = i+1


    #render frequency
    frequency = klaviatur[synthie[takt]]

    if frequency < 1:				#if notone
        frequency = 1
        speaker.duty_cycle = 0
    else:							#if tone
        speaker.duty_cycle=2**15
        # add LFO
        mod_freq = max(map_value(analog_in.value, 300, 65535, 2,300),0)
        mod_amp = max(map_value(analog_in2.value, 300, 65535, 0,1000),0)       
        frequency = max(frequency + (math.sin(time.monotonic()*mod_freq))*mod_amp,1)
    #time.sleep(0.00001) # little delay for stability
    
        print(mod_amp)
    speaker.frequency = int(frequency)

