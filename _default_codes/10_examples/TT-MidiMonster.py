##### MIDI MONSTER Control BOXXXX###############
import board, digitalio, busio, time, pwmio, adafruit_midi, neopixel, pulseio, audiopwmio, audiocore
from adafruit_midi.note_off import NoteOff
from adafruit_midi.note_on import NoteOn
from adafruit_simplemath import map_range
from adafruit_motor import motor
from adafruit_motor import servo

midichannel = 4



time.sleep(2)

# UART-Initialisierung für MIDI-Kommunikation
uart = busio.UART(tx=board.GP12, rx=board.GP13, baudrate=31250, timeout=0.001)
midi = adafruit_midi.MIDI(midi_in=uart, in_channel=midichannel-1)

#SETUP

led = digitalio.DigitalInOut(board.GP27)		# LED
led.direction = digitalio.Direction.OUTPUT

#speaker_pin = board.GP3
freq = [31, 33, 35, 37, 39, 41, 44, 46, 49, 52, 55, 58, 62, 65, 69, 73, 78, 82, 87, 93, 98, 104, 110, 117, 123, 131, 139, 147, 156, 165, 175, 185, 196, 208, 220, 233, 247, 262, 277, 294, 311, 330, 349, 370, 392, 415, 440, 466, 494, 523, 554, 587, 622, 659, 698, 740, 784, 831, 880, 932, 988, 1047, 1109, 1175, 1245, 1319, 1397, 1480, 1568, 1661, 1760, 1865, 1976, 2093, 2217, 2349, 2489, 2637, 2794, 2960, 3136, 3322, 3520, 3729, 3951, 4186, 4435, 4699, 4978]

motor = motor.DCMotor(pwmio.PWMOut(board.GP0, frequency=50), pwmio.PWMOut(board.GP1, frequency=50))

pwm = pwmio.PWMOut(board.GP15, duty_cycle=2 ** 15, frequency=50)			# SPEAKER
my_servo = servo.Servo(pwm)

wav_file = audiocore.WaveFile(open("mau.wav", "rb"))
audio = audiopwmio.PWMAudioOut(board.GP4)

speaker = pwmio.PWMOut(board.GP3, duty_cycle=0, variable_frequency=True)

moon = neopixel.NeoPixel(board.GP14, 1, brightness=1, auto_write=False) 	# MOON
pixels = neopixel.NeoPixel(board.GP26, 30, brightness=1, auto_write=False) 	# LED STRIEFEN


# Startup Animation
for i in range(5):
    moon.fill((0,50*i,255-(50*i)))
    moon.show()
    time.sleep(0.2)
    moon.fill((0,0,0))
    moon.show()
    time.sleep(0.2)

def MIDIon(note):

    pxValue = int(map_range(note, 41, 72, 0, 255))			#MOON
    moon.fill((pxValue,255-pxValue,0))
    moon.show()
    
    my_servo.angle = int(map_range(note, 41, 72, 0, 180))	# SERVO

    motor.throttle = map_range(note, 41, 72, 0, 100)/100	# MOTOR
    
    speaker.duty_cycle = msg.velocity * 256      # 2 ** 15
    speaker.frequency = freq[note]							#SPEAKER
    
    audio.play(wav_file)
    
    led.value = 1											#LED
    
    pxPos = int(map_range(note, 41, 72, 0, 29))				#LED Streifen  
    pixels[pxPos] = (255-(msg.velocity*2),0,msg.velocity*2)
    pixels.show()
    

    

    

def MIDIoff():
    motor.throttle = 0
    led.value = 0
    moon.fill((0,0,0))
    moon.show()
    pixels.fill((0,0,0))
    pixels.show()
    speaker.frequency = 1
    speaker.duty_cycle = 0
   
# Endlosschleife zum Empfangen von MIDI-Nachrichten um diese zu verarbeiten
while True:
    msg = midi.receive()  # MIDI-Nachricht empfangen

    # Wenn NoteOn-Nachricht empfangen wird
    if (isinstance(msg, NoteOn)):
        # Bei Velocity (Anschlagstärke) 0 als NoteOff interpretieren, manche MIDI-Geräte senden statt "NoteOff" nur "NoteOnn" mit Velocity (Anschlagstärke)=0
        if msg.velocity == 0:
            
            try:print ("Note Off:\t",msg.note,"\t",msg.velocity)
            except:pass
            MIDIoff()
        # Ansonsten als NoteOn ausgeben
        else:
            try:print ("Note On: \t",msg.note,"\t",msg.velocity)
            except:pass
            MIDIon(msg.note)

    # Wenn NoteOff-Nachricht empfangen wird
    if (isinstance(msg, NoteOff)):
        try:print ("Note Off:\t",msg.note,"\t",msg.velocity)
        except:pass
        MIDIoff()







