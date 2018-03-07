import sys

class ContactBook:
	def __init__(self):
		print('''
			______________________________________________________________
			 _____             _             _    ______             _ 
			/  __ \           | |           | |   | ___ \           | |
			| /  \/ ___  _ __ | |_ __ _  ___| |_  | |_/ / ___   ___ | | __
			| |    / _ \| '_ \| __/ _` |/ __| __| | ___ \/ _ \ / _ \| |/ /
			| \__/\ (_) | | | | || (_| | (__| |_  | |_/ / (_) | (_) |   <
			 \____/\___/|_| |_|\__\__,_|\___|\__| \____/ \___/ \___/|_|\_\

			______________________________________________________________
		''')

	def start(self):
		while True:
			print(''' 
				Select a option:

				[1]: Add contact
				[2]: Update contact
				[3]: Search contact
				[4]: Delete contact
				[5]: List contacts
				[6]: Back to main menu
				[7]: Exit
			''')
			try:
				method = int(input("\nYour option: "))
				if method == 1: 
					pass
				elif method == 2: 
					pass
				elif method == 3: 
					pass
				elif method == 4: 
					pass
				elif method == 5: 
					pass
				elif method == 6:
					break
				elif method == 7:
					sys.exit()
				else:
					print("\nCommand not found")
					continue
				
				# while True:
				# 	number = int(input("\nWrite a number: "))
				# 	self.start_time = time.time()
				# 	self.search(number, 0, len(self.numbers) - 1)
				# 	break

			except ValueError:
				print("\nCommand not found")
				continue