import adafruit_simplemath, time

# ---- BASIC FUNCTIONS ---- #
def foo(x):
    print("X is {}".format(x))

while True:
    foo(5)
    time.sleep(2)

# ---- IF STATEMENT ---- #
    if 5 < 8:
        print("five is greater than eight")
    time.sleep(2)

# ---- FOR LOOP from 13 to 99 ---- #
    for i in range(13, 100):
        print(i)
        time.sleep(0.05)
        
# ---- WHILE LOOP ---- #
    x=0
    while x <= 50:
        print(x)
        time.sleep(0.1)
        x += 1
        


