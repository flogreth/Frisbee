## --------  PWM TÖNE SPIELEN  -------- ##
#    tested with tinkertanks frisbee     #

import board, time, pwmio

speaker = pwmio.PWMOut(board.GP0, duty_cycle=2**15, variable_frequency=True)
speaker.frequency = 5


while True:
    
    for i in range(100):
        speaker.frequency = i*100 +0.1 
        print(i)
        speaker.duty_cycle = 6000  # 0.5 bestimmt die Lautstärke (oder so)
        time.sleep(0.01)

        speaker.duty_cycle = 0
        time.sleep(0.01)
    
    

