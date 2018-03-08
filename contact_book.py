import sys

class Contact:
	def __init__(self, name, phone, email):
		self.name = name.strip()
		self.phone = phone.strip()
		self.email = email.strip()

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
					self.update()
				elif method == 3: 
					self.search()
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
		contacts = [self._print_contact(contact) for contact in self._contacts]
		if not len(contacts): print('\nThere are no added contacts')

	def update(self):
		contact_old = self.search()
		if contact_old:
			name = contact_old.name
			phone = contact_old.phone
			email = contact_old.email

			while True:
				print(''' 
					Update contact:

					[1]: Name
					[2]: Phone
					[3]: Email
					[4]: All information
				''')

				try:
					method = int(input("\nYour option: "))
					if method == 1: 
						name = str(input('\nWrite a name: '))
					elif method == 2:
						phone = str(input('\nWrite a phone: '))
					elif method == 3:
						email = str(input('\nWrite a email: '))
					elif method == 4:
						name = str(input('\nWrite a name: '))
						phone = str(input('\nWrite a phone: '))
						email = str(input('\nWrite a email: '))
					else:
						print("\nCommand not found")
						continue

					contact_new = Contact(name, phone, email)
					
					for idx, contact in enumerate(self._contacts):
						if contact.name.lower() == contact_old.name.lower():
							self._contacts[idx] = contact_new
							self._print_contact(contact_new)
							break
					break

				except ValueError:
					print("\nCommand not found")
					continue


	def search(self):
		name = str(input('\nWrite a name: ')).strip()
		for contact in self._contacts:
			if contact.name.lower() == name.lower():
				self._print_contact(contact)
				return contact
		else:
			print('\nContact not found')
			return False

	def _print_contact(self, contact):
		print('\n--- * --- * ---- * ---- * ---- * ---- * ----')
		print('Nombre: {}'.format(contact.name))
		print('Teléfono: {}'.format(contact.phone))
		print('Email: {}'.format(contact.email))
		print('--- * --- * ---- * ---- * ---- * ---- * ----')