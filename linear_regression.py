import sys
import random

class LinearRegression:
    def __init__(self):
        print('''
            _________________________________________________________________________________
             _     _                        ______                             _             
            | |   (_)                       | ___ \                           (_)            
            | |    _ _ __   ___  __ _ _ __  | |_/ /___  __ _ _ __ ___  ___ ___ _  ___  _ __  
            | |   | | '_ \ / _ \/ _` | '__| |    // _ \/ _` | '__/ _ \/ __/ __| |/ _ \| '_ \ 
            | |___| | | | |  __/ (_| | |    | |\ \  __/ (_| | | |  __/\__ \__ \ | (_) | | | |
            \_____/_|_| |_|\___|\__,_|_|    \_| \_\___|\__, |_|  \___||___/___/_|\___/|_| |_|
                                                        __/ |                                
                                                       |___/                                 
            _________________________________________________________________________________
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
                
                pending = self.get_pending(self.numbers)
                point_intersection = self.get_point_intersection(self.numbers, pending)
                self.get_prediction(self.numbers, pending, point_intersection)

            except ValueError:
                print("\nCommand not found")
                continue

    def random_numbers(self):
        self.numbers = { x: random.randint(1,50) for x in range(random.randint(1,10)) }
        return self.print_numbers()

    def manual_numbers(self):
        while True:
            self.numbers = {}
            try:
                values = list((map(int, str(input("\nWrite values separated by comma: ")).split(','))))
                if len(values) == 1: raise ZeroDivisionError
                self.numbers = {idx + 1: value for idx, value in enumerate(values)}
                return self.print_numbers()
            
            except ValueError:
                print("\nPlease, just integers numbers seperated by coma.")
            
            except ZeroDivisionError:
                print("\nPlease, write more than one number")
    
    def print_numbers(self):
        print("\nGenerated Sample:")
        {print("\n{} => {}".format(key, val)) for key, val in self.numbers.items()}

    def get_pending(self, sample):
        summatory_key_x_val = sum([(key * val) for key, val in sample.items()])
        summatory_val = sum(sample.values())
        summatory_key = sum(sample.keys())
        summatory_key_square = sum([key ** 2 for key in sample.keys()])
        dividend = (len(sample) * summatory_key_x_val) - (summatory_val * summatory_key)
        divider = (len(sample) * summatory_key_square) - (summatory_key ** 2)
        return dividend / divider

    def get_point_intersection(self, sample, pending):
        mid_values = sum(sample.values()) / len(sample)
        mid_keys = sum(sample.keys()) / len(sample)
        return mid_values - (pending * mid_keys)

    def get_prediction(self, sample, pending, point_intersection):
        while True:
            try:
                time_frame = int(input("\nWrite a index of prediction: "))
                if time_frame <= list(sample.keys())[-1]:
                    raise IndexError
                prediction = point_intersection + (pending * time_frame)
                print("\nThe prediction is {}".format(prediction))
                question = "\nDo you want to look for another prediction (Y/N): "
                if not self.choose_yes_or_not(question): break
            
            except IndexError:
                print("\nTry with a greater number than {}".format(list(sample.keys())[-1]))
            
            except ValueError:
                print("\nPlease, just numbers")


    def choose_yes_or_not(self, question):
        while True:
            answer = str(input(question)).lower()
            if answer == 'n':
                return False
            elif answer == 'y':
                return True
            else:
                print("\n Command not found")
                continue