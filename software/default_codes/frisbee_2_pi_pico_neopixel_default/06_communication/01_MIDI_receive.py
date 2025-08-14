 # Dies ist ein Grundgerüst um MIDI-Signale auf dem Moon zu empfangen und zu verarbeiten.
 # Der Moon erhält dabei drei Variablen (NoteOn/-Off, note, velocity) die er weiterverarbeiten kann.  
import board
import digitalio
import busio
import adafruit_midi
from adafruit_midi.note_off import NoteOff
from adafruit_midi.note_on import NoteOn

# UART-Initialisierung für MIDI-Kommunikation
uart = busio.UART(tx=board.GP12, rx=board.GP13, baudrate=31250, timeout=0.001)
midi = adafruit_midi.MIDI(midi_in=uart, in_channel=0)

# GND-Pin initialisieren und auf 0V setzen
gnd = digitalio.DigitalInOut(board.GP2)
gnd.direction = digitalio.Direction.OUTPUT
gnd.value = False

# Endlosschleife zum Empfangen von MIDI-Nachrichten um diese zu verarbeiten
while True:
    msg = midi.receive()  # MIDI-Nachricht empfangen

    # Wenn NoteOn-Nachricht empfangen wird
    if (isinstance(msg, NoteOn)):
        # Bei Velocity (Anschlagstärke) 0 als NoteOff interpretieren, manche MIDI-Geräte senden statt "NoteOff" nur "NoteOnn" mit Velocity (Anschlagstärke)=0
        if msg.velocity == 0:
            print ("Note Off:\t",msg.note,"\t",msg.velocity)
        # Ansonsten als NoteOn ausgeben
        else:
            print ("Note On: \t",msg.note,"\t",msg.velocity)

    # Wenn NoteOff-Nachricht empfangen wird
    if (isinstance(msg, NoteOff)):
        print ("Note Off:\t",msg.note,"\t",msg.velocity)