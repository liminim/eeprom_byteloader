#!/usr/bin/env/python3


import serial.tools.list_ports



port_list = []


def get_ports():
    
    ports = serial.tools.list_ports.comports()
    p_list = []
    
    for port, desc, hwid in sorted(ports):
        p_list.append([port, desc, hwid])
        
    if len(p_list) > 0:
        return p_list
    
    else:
        print("!ERROR! - Port list empty. Zero (0) ports found!")
        p_list = [["EMPTY", "EMPTY", "EMPTY"]]
        return p_list
    
    
def num_ports(p_list):
    
    return len(p_list)
    

def print_ports(p_list):
    
    for port, desc, hwid in p_list:
        this_port_index = p_list.index([port, desc, hwid])
        this_port_info = (this_port_index, port, desc, hwid)
        print("\n{}: PORT: {}; DESCRIPTION: {};\nHWID: [{}]\n".format(\
        *this_port_info))


def select_port(p_list):
    
    
    port_list = get_ports()
    print_ports(p_list)
    port_sel = int(input("\nSelect a port using its listed index [999 to EXIT]: "))
    
    if not (port_sel > len(p_list) or port_sel < 0):
        return p_list[port_sel][::]
        
    elif port_sel == 999:
        print("NOTICE: Exiting without selection")
    
    else:
        print("!ERROR! - Invalid Input")
    
    return (-1, -1)


run = True

if __name__ == '__main__':
    
    while run:
        port_list = get_ports()
        
        try:
            selection = int(input("Selection:\n[1]: SELECT an active port.\n[2]: EXIT program.\n"))
        
        # Attempt to get input from user
        except ValueError:
            print("!ERROR! Invalid Input -- Only integers allowed")
        
        # Failsafe to -1 numeric error code
        finally:
            selection = -1
        
        if selection == 1:
            my_port, index = select_port(port_list)
            if index >= 0:
                
                print(my_port)
                print(index)
                
                print("-- Selected Port --\nIndex: [" + str(index) + "]: " + \
                      "Port: {}\nDesc: {}; HWID: [{}]".format(*my_port))
            
        elif selection == 2:
            run = False
            continue
            
        else:
            print("!ERROR! - Invalid selection.")
            
    print("Program is exiting... Goodbye!")
    exit()
