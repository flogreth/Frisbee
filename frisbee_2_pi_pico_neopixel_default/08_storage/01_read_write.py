## -------  STORAGE -------- ##

# !! boot.py muss auch auf den pico gezogen werden

import board

# read from file

file=open('content.txt','r')
content = file.readline()
file.close()

# write to file
file=open('content.txt','w')
file.write(str(bestLap+300))
file.close()
