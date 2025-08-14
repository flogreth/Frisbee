## ----  RFID (Grove Sensor 125KHz)  ---- ##
#     tested with tinkertanks frisbee      #

import time, board, busio

uart = busio.UART(board.GP12, board.GP13, baudrate=9600)

print("Scanning for RFID tags...")
while True:
    if uart.in_waiting > 0:
        data = uart.read(uart.in_waiting)
        print("Received:", data)
        
        if data == b'\x020600562BACD7\x03':
            print("korrekt")
        else:
            print("inkorrekt")
    time.sleep(0.5)
