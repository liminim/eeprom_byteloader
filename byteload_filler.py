#!/usr/bin/env python3


MAX_BYTES = 64000



def buf_limit_check(buffer):
    if buffer > MAX_BYTES:
        print("!ERROR - CAN'T WRITE TO BUFFER - MAX BYTES REACHED!")
        return True
    
    else:
        return False

def buf_write_filter(addr):
    if not buf_limit_check(addr):
        return True
    else:
        return False


if (__name__) == '__main__':
    
    curr_addr = 0
    byte_buffer = []
    
    # Shift byte to left for 8 bytes
    curr_byte = 1
    for x in range(8):
        if buf_write_filter(curr_addr):
            byte_buffer.append(curr_byte)
        curr_byte <<= 1
        curr_addr += 1
    
    # Shift byte to right for 8 bytes
    curr_byte = 128
    for x in range(8):
        if buf_write_filter(curr_addr):
            byte_buffer.append(curr_byte)
        curr_byte >>= 1
        curr_addr += 1

    # Binary count up to 255 (11111111)
    curr_byte = 0
    for x in range(255):
        if buf_write_filter(curr_addr):
            byte_buffer.append(curr_byte)
        curr_byte += 1
        curr_addr += 1
        
    # Binary count down from 255 to 0
    curr_byte = 255
    for x in range(255):
        if buf_write_filter(curr_addr):
            byte_buffer.append(curr_byte)
        
        if curr_byte >=0:
            curr_byte -= 1
        else:
            curr_byte = 0
        curr_addr += 1
    
    hex_array = []
    for byte in byte_buffer:
        hex_array.append(hex(byte))
    print(hex_array)
    
    with open('byteload_test.ackprom', 'ab') as fdump:
        to_bytes = bytes(byte_buffer)
        fdump.write(to_bytes)
    
    buffer_length = len(byte_buffer)
    print("Write Complete!\nWrote " + str(buffer_length) + " bytes!")
