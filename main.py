#!/usr/bin/env/python3
'''main_menu.py - Handles top level menu of eeprom_byteloader.py 
    program. Also handles storing values between sessions.'''


import shelve, os, struct

import serial_com
import port_select as p_sel



DATA_FILE = 'COM_SAVE'
COM_PORT_ATTR = 'port'
COM_DESC_ATTR = 'desc'
COM_HWID_ATTR = 'hwid'
COM_BAUD_ATTR = 'baud'
TARGET_FILE_ATTR = 'target'



def save_COM(port, desc, hwid, baud=9200):
    
    com_save = shelve.open(DATA_FILE)
    
    com_save[COM_PORT_ATTR] = port
    com_save[COM_DESC_ATTR] = desc
    com_save[COM_HWID_ATTR] = hwid
    com_save[COM_BAUD_ATTR] = baud
    
    print('COM Data saved...')
    
    com_save.close()
    

def save_file(file_path):
    
    com_save = shelve.open(DATA_FILE)
    com_save[TARGET_FILE_ATTR] = file_path
    print('File path saved...')
    
    com_save.close()


def read_data():
    com_save = shelve.open(DATA_FILE)
    
    data = (com_save.get(COM_PORT_ATTR), \
           com_save.get(COM_DESC_ATTR), \
           com_save.get(COM_HWID_ATTR), \
           com_save.get(TARGET_FILE_ATTR))
    
    com_save.close()
    
    return data
    
    
def sel_file():
    
    b_file = input ('Enter binary file for transfer: \n\n::> ')
    
    os.system('clear')
    
    if os.path.exists(b_file):
        return b_file
    
    else:
        print('!ERROR! - File not found or does not exist!')

    return -1


def begin_serial():
    
    data = read_data()
    ser = serial_com.SerialCOM(data[0])
    
    if not ser.setup_serial():
        print('!ERROR! - Couldn\'t set up serial connection')
        return False
    
    with open(data[-1], 'rb') as bfile:
        bdata = bytearray(bfile.read())
        ser.load_buffer(bdata)
    
    ser.send_serial()
    
    
    

def menu():
    
    # Gather serial COM port info using port_select.py
    port_info = p_sel.get_ports()
    
    data = read_data()
    data_temp = []
    for i in data: data_temp.append(i)
    
    # Print main menu
    print('''    
                    ######--EEPROM BYTELOADER--######
    
            With an active port selected, choose a binary file
            to upload to Arduino, which will write to EEPROM.
    ---COM---
    PORT: {}
    DESC: {}
    HWID: [{}]
    
    ---FILE---
    Target File: {}\n'''.format(*data_temp))
    
    print('''
    Detected COM ports -- {}'''.format(len(port_info)))
    
    
    print('''
[1] - Configure COM Port
[2] - Select Target File
[3] - Begin Data Transfer
[4] - Quit Program\n''')
    
    try:
        selection = int(input('Make a selection:  '))
    
    except ValueError:
        os.system('clear')
        print('!!ERROR!! - input must be a number!\n')
        return -2
    
    os.system('clear')
    # Select port
    if selection == 1:
        my_port = p_sel.select_port(port_info)
        if my_port != -1:
            save_COM(*my_port)
    
    # Select file
    elif selection == 2:
        target_file = sel_file()
        if target_file != -1:
            save_file(target_file)
    
    # Begin data transfer
    elif selection == 3:
        begin_serial()
    
    # Exit menu
    elif selection == 4:
        print('Exiting...')
        return -1
    
    else:
        print('!ERROR! - INVALID INPUT')
        


if __name__ == '__main__':
    
    run = True
    while run:
        
        if menu() == -1:
            run = False

print('\n\nExiting program... Goodbye!\n\n')
