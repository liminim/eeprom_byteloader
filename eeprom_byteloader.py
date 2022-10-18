#!/usr/bin/env python3


import serial
from time import sleep

import main_menu


MAX_PAGE_BYTES = 128
MAX_BYTES = 64000

byte_buffer = []
page_buffer = []
        

def serial_xfer_begin():
    """ !!DISABLED FOR TESTING!!
    ser = serial.Serial('/dev/ttyACM0', 19200, timeout=0.5)
    ser.reset_input_buffer()
    
    while ser.in_waiting:
        ser.write(b"Hello dickless!\n")
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
        time.sleep(0.5)
    """


run = True

if __name__ == '__main__':
    
    while run:
        
        menu_result = main_menu.menu()
        
        if menu_result == -1:
            run = False
            continue
        
        elif menu_result == 2:
            serial_xfer_begin()
