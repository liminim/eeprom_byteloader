#!/usr/bin/env python3


import serial
import shelve
from time import sleep
from os.path import exists

import port_select as p_sel
import main_menu


MAX_PAGE_BYTES = 128
MAX_BYTES = 64000

byte_buffer = []
page_buffer = []

DATA_FILE = 'COM_SAVE'
COM_PORT_ATTR = 'port'
COM_DESC_ATTR = 'desc'
COM_HWID_ATTR = 'hwid'



def save_com(port="None", desc="None", hwid="None"):
    
    com_save = shelve.open(DATA_FILE)
    
    com_save[COM_PORT_ATTR] = port
    com_save[COM_DESC_ATTR] = desc
    com_save[COM_HWID_ATTR] = hwid
    
    com_save.close()


def read_COM():
    com_save = shelve.open(DATA_FILE)
    
    data = (com_save.get(COM_PORT_ATTR), \
           com_save.get(COM_DESC_ATTR), \
           com_save.get(COM_HWID_ATTR))
    
    com_save.close()
    
    return data
        

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
        
        menu_result = menu()
        
        if menu_result == -1:
            run = False
            continue
        
        elif menu_result == 2:
            serial_xfer_begin()
