import sys

class Contact:
	def __init__(self, name, phone, email):
		self.name = name
		self.phone = phone
		self.email = email

class ContactBook:
	def __init__(self):
		self._contacts = []

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
					self.add()
				elif method == 2: 
					pass
				elif method == 3: 
					pass
				elif method == 4: 
					pass
				elif method == 5: 
					self.show_all()
				elif method == 6:
					break
				elif method == 7:
					sys.exit()
				else:
					print("\nCommand not found")
					continue

			except ValueError:
				print("\nCommand not found")
				continue

	def add(self):
		name = str(input('\nWrite a name: '))
		phone = str(input('\nWrite a phone: '))
		email = str(input('\nWrite a email: '))
		self._contacts.append(Contact(name, phone, email))

	def show_all(self):
		[self._print_contact(contact) for contact in self._contacts]

	def _print_contact(self, contact):
		print('\n--- * --- * ---- * ---- * ---- * ---- * ----')
		print('Nombre: {}'.format(contact.name))
		print('Teléfono: {}'.format(contact.phone))
		print('Email: {}'.format(contact.email))
		print('--- * --- * ---- * ---- * ---- * ---- * ----')