import sys
import random
import math

class VarianceDeviation:
	def __init__(self):
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
					self.get_standard_deviation(self.get_variance(self.numbers))
				elif method == 2: 
					pass
				elif method == 3:
					break
				elif method == 4:
					sys.exit()
				else:
					print("\nCommand not found")
					continue

			except ValueError:
				print("\nCommand not found")
				continue

	def random_numbers(self):
		self.numbers = [random.randint(1,101) for x in range(random.randint(2,5))]
		return self.numbers

	def get_variance(self, sample):
		variance = round(sum([(number - sum(sample) / len(sample)) **2 for number in sample]) / (len(sample) - 1), 2)
		print('The variance of {} is {}'.format(sample, variance))
		return variance

	def get_standard_deviation(self, variance):
		standard_deviation = round(math.sqrt(variance), 2)
		print('The standard_deviation of {} is {}'.format(self.numbers, standard_deviation))
		return standard_deviation