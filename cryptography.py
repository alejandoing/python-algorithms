import sys

class Cryptographer:
	def __init__(self):
		print('''
			___________________________________________________________________
			 _____                  _                              _           
			/  __ \                | |                            | |          
			| /  \/_ __ _   _ _ __ | |_ ___   __ _ _ __ __ _ _ __ | |__  _   _ 
			| |   | '__| | | | '_ \| __/ _ \ / _` | '__/ _` | '_ \| '_ \| | | |
			| \__/\ |  | |_| | |_) | || (_) | (_| | | | (_| | |_) | | | | |_| |
			 \____/_|   \__, | .__/ \__\___/ \__, |_|  \__,_| .__/|_| |_|\__, |
			             __/ | |              __/ |         | |           __/ |
			            |___/|_|             |___/          |_|          |___/
			___________________________________________________________________
		''')
	
	def start(self):
		while True:
			print(''' 
				Select a option:

				[1]: Cypher
				[2]: Decypher
				[3]: Back to main menu
				[4]: Exit
			''')

			option = str(input('Your option: '))
			
			if option == '1':
				self.cypher()
			elif option == '2':
				self.decypher()
			elif option == '3':
				break
			elif option == '4':
				print('\nThanks for using Python Algorithms.')
				sys.exit()
			else:
				print('\nCommand not found.')
	
	def cypher(self):
		message = str(input('\nWrite a message: '))
		result = ' '.join(format(ord(letter), 'b') for letter in message)
		print('\nYour message has been crypted to {}'.format(result))

		while True:
			question = str(input('\nDo you want to cypher another message? (Y/N): ')).lower()
			if question == 'y': 
				self.cypher()
			elif question == 'n':
				self.start()
			print('\nCommand not found. Please enter Y or N.')


	def decypher(self):
		code = str(input('Write a crypted code in bytes: ')).strip()
		
		if len(code) < 7:
			print('Please, write a crypted code IN BYTES')
			return self.decypher()
		
		bytes = code.split(' ')
		try:
			decypher_message = [str(chr(int(byte, 2))) for byte in bytes]
			result = ''.join(decypher_message).strip()
		except:
			print('Please, write a crypted code IN BYTES')
			return self.decypher()
		
		if len(result) < 2:
			print('I have not been able to decipher your message. Try something different')
			return self.decypher()
		return print('Your code has been decrypted as: {}'.format(result))