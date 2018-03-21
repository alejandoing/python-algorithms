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
                method = int(input("\nYour option:"))
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
                
                self.print_numbers()

            except ValueError:
                print("\nCommand not found")
                continue

    def random_numbers(self):
        self.numbers = { random.randint(1,1001): random.randint(1,1001) for x in range(random.randint(2,10)) }
        return self.numbers

    def manual_numbers(self):
        self.numbers = {}
        try:
            keys = list((map(int, str(input("\nWrite keys separated by comma: ")).split(','))))
            values = list((map(int, str(input("\nWrite values separated by comma: ")).split(','))))
            self.numbers = {key: values[idx] for idx, key in enumerate(keys)}
            return self.numbers
        
        except ValueError:
            print("\nPlease, just integers numbers seperated by coma.")
            self.numbers = {}
            return self.manual_numbers()

        except IndexError:
            print("\nMust write the same number of elements")
            self.numbers = {}
            return self.manual_numbers()
    
    def print_numbers(self):
        print("\nGenerated Sample:")
        {print("\n{} => {}".format(key, val)) for key, val in self.numbers.items()}