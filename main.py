from cryptography import Cryptographer
from binary_search import BinarySearch

def start():
	print('''  
      __^__                                      __^__
     ( ___ )------------------------------------( ___ )
      | / |                                      | \ |
      | / |   Welcome to the Python Algorithms   | \ |
      |___|           by Alejandoing             |___|
     (_____)------------------------------------(_____) 
    ''')

	print('''Please, select a option to get started: 
		[1] - Cryptography
		[2] - Binary Search
		[3] - Hanged
		[4] - Contact Book
		[5] - Variance and Standard Deviation
		[6] - Coming soon...
		[7] - Coming soon...
		[8] - Coming soon...
		[9] - Coming soon...
		[10] - Coming soon...
		[11] - Coming soon...
		[12] - Coming soon...
		[13] - Coming soon...
		[14] - Coming soon...
		[15] - Coming soon...
		[16] - Coming soon...
		[17] - Coming soon...
		[18] - Coming soon...
		[19] - Coming soon...
		[20] - Coming soon...
	''')
	
	while True:
		try:
			option = int(input('Your option: '))
		except ValueError: 
			print('No letters or special characters are permitted')
			continue
		run_program(option)
		start()

def run_program(option):
	programs = { 1: Cryptographer, 2: BinarySearch }
	return programs[option]().start()
	
if __name__ == '__main__':
	start()