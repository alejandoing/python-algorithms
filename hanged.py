import sys
import random

class Hanged:
    def __init__(self):
        print('''
            ____________________________________
             _   _                            _ 
            | | | |                          | |
            | |_| | __ _ _ __   __ _  ___  __| |
            |  _  |/ _` | '_ \ / _` |/ _ \/ _` |
            | | | | (_| | | | | (_| |  __/ (_| |
            \_| |_/\__,_|_| |_|\__, |\___|\__,_|
                                __/ |
                                |___/
            ____________________________________
        ''')
        self.images = ['''
            +---+
            |   |
                |
                |
                |
                |
            =========''', '''
            +---+
            |   |
            O   |
                |
                |
                |
            =========''', '''
            +---+
            |   |
            O   |
            |   |
                |
                |
            =========''', '''
            +---+
            |   |
            O   |
           /|   |
                |
                |
            =========''', '''
            +---+
            |   |
            O   |
           /|\  |
                |
                |
            =========''', '''
            +---+
            |   |
            O   |
           /|\  |
           /    |
                |
            =========''', '''
            +---+
            |   |
            O   |
           /|\  |
           / \  |
                |
            ========='''
        ]

        self.words = ['lavadora', 'secadora', 'sofa', 'gobierno', 'diputado', 'democracia', 'computadora']
        self.tries = 0
        self.word = None
        self.hidden_word = None

    def start(self):
        self.word = self.random_word()
        self.hidden_word = ['-'] * len(self.word)
        while True:
            self.display_board()
            current_letter = str(input('Write a letter: '))
            self.tries += 1
            # try:
            #     method = int(input("\nYour option: "))
            #     if method == 1: 
            #         pass
            #     elif method == 2: 
            #         pass
            #     elif method == 3:
            #         break
            #     elif method == 4:
            #         sys.exit()
            #     else:
            #         print("\nCommand not found")
            #         continue
                
            #     # while True:
            #     #   number = int(input("\nWrite a number: "))
            #     #   self.start_time = time.time()
            #     #   self.search(number, 0, len(self.numbers) - 1)
            #     #   break

            # except ValueError:
            #     print("\nCommand not found")
            #     continue

    def random_word(self):
        index = random.randint(0, len(self.words) - 1)
        return self.words[index]

    def display_board(self):
        print(self.images[self.tries])
        print("\n {}".format(self.hidden_word))
        print('--- * --- * --- * --- * --- * ---')