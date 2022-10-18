#!/usr/bin/env/python3
"""main_menu.py - Handles top level menu of eeprom_byteloader.py 
    program. Also handles storing values between sessions."""


import shelve

import os

import port_select as p_sel


DATA_FILE = 'COM_SAVE'
COM_PORT_ATTR = 'port'
COM_DESC_ATTR = 'desc'
COM_HWID_ATTR = 'hwid'
TARGET_FILE_ATTR = 'target'



def save_COM(t_file="None", port="None", desc="None", hwid="None"):
    
    com_save = shelve.open(DATA_FILE)
    
    com_save[COM_PORT_ATTR] = port
    com_save[COM_DESC_ATTR] = desc
    com_save[COM_HWID_ATTR] = hwid
    com_save[TARGET_FILE_ATTR] = t_file
    
    print("COM Data saved...\n")
    
    
    com_save.close()


def read_COM():
    com_save = shelve.open(DATA_FILE)
    
    data = (com_save.get(COM_PORT_ATTR), \
           com_save.get(COM_DESC_ATTR), \
           com_save.get(COM_HWID_ATTR), \
           com_save.get(TARGET_FILE_ATTR))
    
    com_save.close()
    
    return data
    
def sel_file():
    
    b_file = input ("Enter binary file for transfer: \n\n::> ")
    
    os.system('clear')
    
    if os.path.exists(b_file):
        
        return b_file
    
    else:
        print("!ERROR! - File not found or does not exist!")
        return "None"


def menu():
    
    # Gather serial COM port info using port_select.py
    port_info = p_sel.get_ports()
    com_data = read_COM()
    com_temp = []
    for i in com_data: com_temp.append(i)
    
    # Print main menu
    print(("\n\n\n    ######--EEPROM BYTELOADER--######\n\n" + \
          "With an active port selected, choose a binary file\n" + \
          "to upload to Arduino, which will write to EEPROM.\n\n" + \
          "           ---COM---\nPORT: [{}]; DESC: [{}];\n" + \
          "HWID: [{}]\n\nTarget File: [{}]").format(*com_temp))
    
    print("Detected COM ports -- {}\n".format(len(port_info)))
    
     
    
    print("[1] - Configure COM Port\n[2] - Select Target File\n" + \
              "[3] - Begin Data Transfer\n[4] - Quit Program\n\n")
    
    # Attempt to gather input from user
    #try:
        #selection = int(input("Make a selection:  "))
    
    #except ValueError:
        #print("!ERROR! Invalid Input -- Only integers allowed")
    # Fail-safe to -1 in case of Value Error
    #finally:
        #selection = -1
    
    selection = int(input("Make a selection:   "))
    # Clear the screen
    os.system("clear")
    
    my_port = []
    if selection == 1:
        my_port = p_sel.select_port(port_info)
    
    elif selection == 2:
        target_file = sel_file()
    
    elif selection == 3:
        my_port = (3, 3)
    
    elif selection == 4:
		# BAD - Change Eventually
        print("Quitting program - Goodbye!\n\n\n")
        exit()
    
    else:
        print("!ERROR! - INVALID INPUT")
        my_port = (0, 0)
    
    save_COM(target_file, *my_port)
    return my_port


if __name__ == '__main__':
    menu()
