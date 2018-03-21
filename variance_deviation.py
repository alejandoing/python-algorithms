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
				elif method == 2: 
					self.manual_numbers()
				elif method == 3:
					break
				elif method == 4:
					sys.exit()
				else:
					raise ValueError
				self.get_standard_deviation(self.get_variance(self.numbers))

			except ValueError:
				print("\nCommand not found")
				continue

	def random_numbers(self):
		self.numbers = [random.randint(1,31) for x in range(random.randint(2,31))]
		print("\nSample: {}".format(self.numbers))
		return self.numbers

	def manual_numbers(self):
		try:
			self.numbers = list(map(int, str(input("\nWrite numbers separated by comma: ")).split(',')))
			return self.numbers
		except ValueError:
			print("\nPlease, just integers numbers seperated by coma.")
			return self.manual_numbers()

	def get_variance(self, sample):
		variance = sum([(number - sum(sample) / len(sample)) **2 for number in sample]) / (len(sample) - 1)
		print('\nThe Variance is {}'.format(variance))
		return variance

	def get_standard_deviation(self, variance):
		standard_deviation = math.sqrt(variance)
		print('The Standard Deviation is {}'.format(standard_deviation))
		return standard_deviation