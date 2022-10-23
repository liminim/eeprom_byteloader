#!/usr/bin/env/python3

import os, serial



class SerialCOM:
	
	def __init__(self, port='undefined', speed=9600, \
		packet_size=16, max_memory=32000):
			
			self.port = port
			self.speed = speed
			self.packet_size = packet_size
			self.max_memory = max_memory
			
			self.buffer = []
	
	
	def __int__(self):
		return len(self.buffer) * self.packet_size
			
			
	def __str__(self):
		return f'''

###--SerialCOM object status--###

TX/RX PORT: {self.port}
BAUD RATE: {self.speed}bps
PACKET SIZE: {self.packet_size}B
MAX MEMORY: {self.max_memory}B
BYTES IN BUFFER: {int(self)}B\n'''
	
	
	def load_buffer(self, data):
		
		packet = []
		
		for b in data:
			if mem_limit():
				print('!!ERROR!! - Buffer at memory limit!')
				break
				
			elif len(packet) == self.packet_size:
				self.buffer.append(packet)
				packet = []
			
			packet.append(b)
	
	
	def mem_limit(self):
		
		if int(self) >= self.max_memory:
			return True
		
		else:
			return False

	

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
		
