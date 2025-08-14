## ------  MP3 DATEIEN ABSPIELEN  ------ ##
#      tested with tinkertanks moon       #

import board, audiomp3, audiopwmio

audio = audiopwmio.PWMAudioOut(board.GP4)					#Lautsprecher an Pin GP4 (D4)
mp3file = audiomp3.MP3Decoder(open("04_sound/miau.mp3", "rb"))

audio.play(mp3file) 										#spielt die MP3

while audio.playing:
    pass 													#warte bis zu ende gespielt

print("Done playing!")