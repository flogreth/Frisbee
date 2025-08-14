

##    ------  NEOPIXEL  ------    ##
#   tested with tinkertanks moon   #

import time, board, neopixel, random, touchio, audiomp3, audiopwmio

audio = audiopwmio.PWMAudioOut(board.GP0)					#Lautsprecher an Pin GP4 (D4)
mp3file = audiomp3.MP3Decoder(open("master.mp3", "rb"))

audio.play(mp3file) 	

#setup
touch_pad_R = board.GP11
touch_R = touchio.TouchIn(touch_pad_R)
touch_R.threshold = 5000

touch_pad_G = board.GP12
touch_G = touchio.TouchIn(touch_pad_G)
touch_G.threshold = 5000

touch_pad_B = board.GP20
touch_B = touchio.TouchIn(touch_pad_B)
touch_B.threshold = 5000

#color definitions
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
MAGENTA = (255,0,255)
YELLOW = (255,255,0)
CYAN = (0,255,255)
WHITE = (255,255,255)
BLACK = (0,0,0)
color_levels = [BLACK,RED,GREEN,BLUE,WHITE,YELLOW,MAGENTA,CYAN]

level = 0

last_update = 0.01
last_drop = 0.01
drop_speed = 0.1
next_drop = 2.8

chord_correct = 0
chord_wrong = 0

difficulty = 2

numpixels = 60
px_value = [0 for x in range(numpixels)]
pixels = neopixel.NeoPixel(board.GP21, numpixels, brightness=1, auto_write=False) #z.B. 1 Pixel an pin GP14 (der Mond)

audio.play(mp3file)

while True:
    

    #update strip
    if (time.monotonic() - last_update) > drop_speed/5 :
        
        # shift pixels one step
        for i in range(numpixels-1):
            px_value[i] = px_value[i+1]
        
        # new pixel drops
        if (time.monotonic() - last_drop) > next_drop :
            px_value[numpixels-1] = random.randint(1,difficulty)
            last_drop = time.monotonic()
        else:
            px_value[numpixels-1] = 0

        # decrement right and wrong lights
        if chord_correct > 0: chord_correct = chord_correct-1
        if chord_wrong > 0: chord_wrong = chord_wrong-1


        # put px_values in pixels
        for i in range(numpixels):
            pixels[i] = color_levels[px_value[i]]
            if px_value[i] == 0:
                pixels[i] = ((chord_wrong*10),(chord_correct*10),0)
        
        #aktueller Chord from touch values
        chord = [touch_R.value, touch_G.value, touch_B.value]
        chord_nr = 0
        if chord == [1,0,0]: chord_nr = 1
        if chord == [0,1,0]: chord_nr = 2
        if chord == [0,0,1]: chord_nr = 3
        if chord == [1,1,1]: chord_nr = 4
        if chord == [1,1,0]: chord_nr = 5
        if chord == [1,0,1]: chord_nr = 6
        if chord == [0,1,1]: chord_nr = 7
        pixels[0] = (chord[0]*255,chord[1]*255,chord[2]*255)
        
        #final show
        pixels.show()

        # hit check color match
        if px_value[0] > 0:
            #print(px_value[0],chord_nr)
            if px_value[0] == chord_nr:
                chord_correct = 5
                level = level + 1
            else:
                chord_wrong = 5
                if level > 1:
                    level = level - 2
            
            # new difficulties and speeds
            difficulty = min( int(level / 9) + 2 , 7) # every 7 levels difficulty increases. min level is 3, max is 7
            drop_speed = -0.0005 * level + 0.1
            
            next_drop = max( 1.8 / (random.random()+1) - level / 120 , 0.2) # starting from 0.8/1.8 to minimum of 0.2
            print (drop_speed, next_drop, difficulty, level)
        

        last_update = time.monotonic()
    time.sleep(0.001)



