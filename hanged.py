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
        self.current_letter = None
        self.letters_used = list()

    def start(self):
        self.word = self.random_word()
        self.hidden_word = ['-'] * len(self.word)
        while True:
            self.display_board()
            self.current_letter = str(input('Write a letter: '))
            if not self.correct_letter(self.current_letter): self.tries += 1
            if self.game_over():
                question = "\n Do you want play again? (Y/N): "
                if not self.choose_yes_or_not(question): break

    def random_word(self):
        index = random.randint(0, len(self.words) - 1)
        return self.words[index]

    def display_board(self):
        print(self.images[self.tries])
        print("\n {}".format(self.hidden_word))
        print('--- * --- * --- * --- * --- * ---')

    def correct_letter(self, current_letter):
        correct = False
        for index in range(len(self.word)):
            if self.word[index] == self.current_letter:
                self.hidden_word[index] = self.current_letter
                correct = True
        return correct

    def has_won(self):
        if not '-' in self.hidden_word:
            self.display_board()
            self.send_message('Congratulations! You have won with a total of {} failures!'.format(self.tries))
            return True

    def has_lost(self):
        if self.tries == 6:
            self.display_board()
            self.send_message('You lost! The word was {}'.format(self.word))
            return True

    def game_over(self):
        self.set_status()
        if self.has_won() or self.has_lost(): return True

    def send_message(self, message):
        print('\n {}'.format(message))

    def set_status(self):
        if not self.current_letter in self.letters_used: self.letters_used.append(self.current_letter)
        self.send_message('Letters used: {}'.format(self.letters_used))
        self.send_message('Tries: {}'.format(len(self.letters_used)))
        if self.tries == 5: self.send_message('WARNING! You have one last attempt.')

    def reset_game(self):
        self.tries = 0
        self.current_letter = None
        self.letters_used = list()
        self.word = self.random_word()
        self.hidden_word = ['-'] * len(self.word)

    def choose_yes_or_not(self, question):
        while True:
            answer = str(input(question)).lower()
            if answer == 'n': return False
            elif answer == 'y':
                self.reset_game()
                return True
            else:
                print("\n Command not found")
                continue