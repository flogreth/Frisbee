## ------  WAV DATEIEN ABSPIELEN  ------ ##
#      tested with tinkertanks moon       #

import board, audiocore, audiopwmio

audio = audiopwmio.PWMAudioOut(board.GP4)					#Lautsprecher an Pin GP4 (D4)
wavfile = audiocore.WaveFile(open("04_sound/miau.wav", "rb"))

audio.play(wavfile) 										#spielt die wav file ab

while audio.playing:
    pass 													#warte bis zu ende gespielt

print("Done playing!")