#!/usr/bin/env/python3



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
          "HWID: [{}]\n").format(*com_temp))
    
    print("Detected COM ports -- {}\n".format(len(port_info)))
    
    print("[1] - Configure COM Port\n[2] - Select Target File\n" + \
              "[3] - Begin Data Transfer\n[4] - Quit Program\n\n")
    
    # Attempt to gather input from user
    try:
        selection = int(input("Make a selection:  "))
    
    except ValueError:
        print("!ERROR! Invalid Input -- Only integers allowed")
    
    # Fail-safe to -1 in case of Value Error
    finally:
        selection = -1
    
    my_port = []
    if selection == 1:
        my_port = p_sel.select_port(port_info)
    
    elif selection == 2:
        #print("Selection 2")
    
    elif selection == 3:
        #print("Selection 3")
    
    elif selection == 4:
		# BAD - Change Eventually
        print("Quitting program - Goodbye!\n\n\n")
        exit()
    
    else:
        print("!ERROR! - INVALID INPUT")
        
    if my_port[0] != -1:
        return my_port
