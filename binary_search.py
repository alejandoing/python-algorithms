import random
import time

class BinarySearch:
	def __init__(self):
		self.numbers = []
		self.start_time = None
		print('''
			__________________________________________________________________
			______ _                          _____                     _     
			| ___ (_)                        /  ___|                   | |    
			| |_/ /_ _ __   __ _ _ __ _   _  \ `--.  ___  __ _ _ __ ___| |__  
			| ___ \ | '_ \ / _` | '__| | | |  `--. \/ _ \/ _` | '__/ __| '_ \ 
			| |_/ / | | | | (_| | |  | |_| | /\__/ /  __/ (_| | | | (__| | | |
			\____/|_|_| |_|\__,_|_|   \__, | \____/ \___|\__,_|_|  \___|_| |_|
									   __/ |                                  
									  |___/                                   
			__________________________________________________________________
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
				while True:
					number = int(input("\nWrite a number: "))
					self.start_time = time.time()
					self.search(number, 0, len(self.numbers) - 1)
				self.numbers = []
			except ValueError:
				print("\nCommand not found")
				continue

	def random_numbers(self):
		self.numbers = sorted(set([random.randint(1,10001) for x in range(random.randint(1,10001))]))
		return print("\nA collection of {} numbers has been generated".format(len(self.numbers)))

	def manual_numbers(self):
		self.numbers = list(map(int, str(input("\nWrite numbers separated by comma: ")).split(',')))
		return print("\nYour collection {} has been generated".format(self.numbers))

	def search(self, number_to_find, low, high):
		elapsed_time = round(time.time() - self.start_time, 5)
		mid = (low + high) // 2
		
		if low > high: 
			return self.print_result(False, 'Number not found', elapsed_time)

		if self.numbers[mid] == number_to_find: 
			return self.print_result(True, 'Number found', elapsed_time)

		elif self.numbers[mid] > number_to_find:
			print("{} is less than {}".format(number_to_find, self.numbers[mid]))
			return self.search(number_to_find, low, mid - 1)

		else:
			print("{} is greater than {}".format(number_to_find, self.numbers[mid]))
			return self.search(number_to_find, mid + 1, high)

	def print_result(self, result, message, time):
		if time == 0.0: 
			print("\n{} without delay!".format(message, time))
		else:
			print("\n{} with {} seconds of delay!".format(message, time))
		return result