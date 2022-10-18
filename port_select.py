#!/usr/bin/env/python3


import serial.tools.list_ports
import os



def get_ports():
    
    ports = serial.tools.list_ports.comports()
    p_list = []
    
    for port, desc, hwid in sorted(ports):
        p_list.append([port, desc, hwid])
        
    if len(p_list) > 0:
        return p_list
    
    else:
        print('!ERROR! - Port list empty. Zero (0) ports found!')
        p_list = [['EMPTY', 'EMPTY', 'EMPTY']]
        return p_list
    
    
def num_ports(p_list):
    
    return len(p_list)
    

def print_ports(p_list):
    
    os.system('clear')
    
    for port, desc, hwid in p_list:
        this_port_index = p_list.index([port, desc, hwid])
        this_port_info = (this_port_index, port, desc, hwid)
        print('''
 {}: 
    PORT: {}
    DESCRIPTION: {}
    HWID: [{}]\n'''.format(*this_port_info))


def select_port(p_list):
    
    # Clear screen
    os.system('clear')
    
    
    print_ports(p_list)
    port_sel = int(input('''
Select a port using its listed index [0 to EXIT]: '''))
    
    os.system('clear')
    
    if not (port_sel > len(p_list) or port_sel < 0):
        return p_list[port_sel]
        
    elif port_sel == 0:
        print('NOTICE: Exiting without selection')
    
    else:
        print('!ERROR! - Invalid Input')
    
    return -1
    

def test():
    port_list = get_ports()
        
    selection = int(input('''\n
port_select.py test:


[1] -- SELECT an active port.
[2] -- EXIT program.\n'''))
    
    os.system('clear')

    if selection == 1:
        my_port = select_port(port_list)
        
        print(''''\n
##--Selected Port--##

Port: {}
Desc: {}
HWID: [{}]'''.format(*my_port))
    
    elif selection == 2:
        return -1
        
    else:
        print('!ERROR! - Invalid selection.')

if __name__ == '__main__':
    
    run = True
    
    while run:
        
        if test() == -1:
            run = False
    os.system('clear')
    print('\n\nProgram is exiting... Goodbye!\n')
