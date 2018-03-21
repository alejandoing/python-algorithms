import sys

class Cryptographer:
	def __init__(self):
		self.starting = True
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

			try:
				option = int(input('Your option: '))
			except ValueError:
				print('\nCommand not found')
				continue
			
			options = {1: self.cypher, 2: self.decypher, 3: False, 4: sys.exit}
			if not self.choose_option(option, options): break
	
	def cypher(self):
		message = str(input('\nWrite a message: '))
		result = ' '.join(format(ord(letter), 'b') for letter in message)
		print('\nYour message has been crypted to {}'.format(result))

		while True:
			options = {'y': self.cypher, 'n': self.start}
			answer = str(input('\nDo you want to cypher another message? (Y/N): ')).lower()
			if not self.choose_option(answer, options): break

	def decypher(self):
		code = str(input('\nWrite a 8 bit ASCII code: ')).strip()
		bytes = code.split(' ')
		
		try:
			decypher_message = [str(chr(int(byte, 2))) for byte in bytes]
			result = ''.join(decypher_message).strip()
			if len(code) < 7: raise ValueError
		except:
			print('\nPlease, just write a 8 bit ASCII codes')
			return self.decypher()
		
		print('\nYour code has been decrypted as: {}'.format(result))
		
		while True:
			options = {'y': self.decypher, 'n': self.start}
			answer = str(input('\nDo you want to decypher another message? (Y/N): ')).lower()
			if not self.choose_option(answer, options): break

	def choose_option(self, selected, options):
		if not self.starting: return False
		
		try:
			return options[selected]()
		except TypeError:
			self.starting = False
			return options[selected]
		except KeyError:
			print('\nCommand not found')
			return True