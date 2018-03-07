import sys
import random

class VarianceDeviation:
	def __init__(self):
		pass

	def start(self):
		print('''
			________________________________________________________________________________________
			                        _   _            _                                              
			                       | | | |          (_)                                             
			                       | | | | __ _ _ __ _  __ _ _ __   ___ ___                         
			                       | | | |/ _` | '__| |/ _` | '_ \ / __/ _ \                        
			                       \ \_/ / (_| | |  | | (_| | | | | (_|  __/                        
			                        \___/ \__,_|_|  |_|\__,_|_| |_|\___\___|                        
			                                                                                        
			                                                                                        
			 _____ _                  _               _  ______           _       _   _             
			/  ___| |                | |             | | |  _  \         (_)     | | (_)            
			\ `--.| |_ __ _ _ __   __| | __ _ _ __ __| | | | | |_____   ___  __ _| |_ _  ___  _ __  
			 `--. \ __/ _` | '_ \ / _` |/ _` | '__/ _` | | | | / _ \ \ / / |/ _` | __| |/ _ \| '_ \ 
			/\__/ / || (_| | | | | (_| | (_| | | | (_| | | |/ /  __/\ V /| | (_| | |_| | (_) | | | |
			\____/ \__\__,_|_| |_|\__,_|\__,_|_|  \__,_| |___/ \___| \_/ |_|\__,_|\__|_|\___/|_| |_|
			________________________________________________________________________________________
		''')

	def start(self):
		while True:
			print(''' 
				Select a option:

				[1]: Random numbers
				[2]: Manual numbers
				[3]: Back to main menu
				[4]: Exit
			''')
			try:
				method = int(input("\nYour option: "))
				if method == 1: 
					self.random_numbers()
				elif method == 2: 
					pass
				elif method == 3:
					break
				elif method == 4:
					sys.exit()
				else:
					print("\nCommand not found")
					continue
				
				# while True:
				# 	number = int(input("\nWrite a number: "))
				# 	#self.start_time = time.time()
				# 	#self.search(number, 0, len(self.numbers) - 1)
				# 	break

			except ValueError:
				print("\nCommand not found")
				continue

	def random_numbers(self):
		self.numbers = [random.randint(1,101) for x in range(random.randint(1,101))]
		print(self.numbers)
		return print("\nA collection of {} numbers has been generated".format(len(self.numbers)))