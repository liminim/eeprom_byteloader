#!/usr/bin/env/python3

import os, serial, time



class SerialCOM:
	
	def __init__(self, port='undefined', speed=9600, \
		 packet_size=16, max_memory=32000, timeout=1):
			
			self.port = port
			self.speed = speed
			self.packet_size = packet_size
			self.max_memory = max_memory
			self.timeout = timeout
			
			self.ser = None
			self.buffer = bytearray()
			self.abort = False
			
	
	def __int__(self):
		buffer_len = len(self.buffer)
		return buffer_len
		
			
		
	def __str__(self):
		return f'''

###--SerialCOM object status--###

TX/RX PORT: {self.port}
BAUD RATE: {self.speed}bps
PACKET SIZE: {self.packet_size}B
MAX MEMORY: {self.max_memory}B
BYTES IN BUFFER: {int(self)}B\n'''


	def mem_limit(self):
		
		if int(self) >= self.max_memory:
			return True
		
		else:
			return False
	
	
	def mem_limit_warn(self):
		
		print('WARNING - Memory limit exceeded. Abort write?')
		
		try:
			sel = int(input('1 - Abort; 2 - Continue: '))
		
		except ValueError:
			print('ERROR - input must be a number')
		
		except:
			print('ERROR - invalid input')
		
		if sel == 1:
			self.abort = True
		
		elif sel == 2:
			self.abort = False
		
	
	def load_buffer(self, data):
		
		self.buffer = []
		
		for b in data:
				
			if self.mem_limit():
				self.mem_limit_warn()
				break
			
			self.buffer.append(b)
	
	
	def send_serial(self, byte_size=8, parity='N', stop_bits=1):
		
		os.system('clear')
		
		if len(self.buffer) == 0:
			print('ERROR - No data in buffer to write')
			return False
		
		if serial == None:
			print('ERROR - Serial object undefined')
			return False
		
		if self.abort:
			print('WARNING - Aborting write...')
			return False
		
		temp_serial = serial.Serial(self.port, self.speed, byte_size, \
			parity, stop_bits)
		time.sleep(3)

		temp_serial.write(self.buffer)
		
		print(self.buffer)
		print(self);
			
	

	def setup_serial(self):
		
		os.system('clear')
		try:
			self.speed = int(input('\nBaud rate: '))
			self.packet_size = int(input('\nEEPROM Buffer Size: '))
			self.max_memory = int(input('\nEEPROM Memory Size: '))
			
		
		except ValueError:
			print('ERROR - Input must be a number')
			return False
		
		
		return True


def test():
	
	com_obj = SerialCOM('my_port[TEST]', 19200, 128, 64000)
	
	print(com_obj)
	print(f'Call as int: {int(com_obj)}\n')
	
	

if __name__ == '__main__':
	
	run = True
	while run:
		
		try:
			sel = int(input('\n[1]-run the test  $  [2]-exit: '))
			
		except ValueError:
			print('!ERROR! - Input must be a number!')
		
		except:
			print('!ERROR! - Invalid input!')
		
		else:
			os.system('clear')
		
			if sel == 2:
				run = False
			
			elif sel == 1:
				test()
			
			else:
				print('Nah not one of the options. Stuck in the loop')
		
