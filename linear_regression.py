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

            except ValueError:
                print("\nCommand not found")
                continue

    def random_numbers(self):
        self.numbers = [random.randint(1,31) for x in range(random.randint(2,31))]
        print("\nSample: {}".format(self.numbers))
        return self.numbers

    def manual_numbers(self):
        try:
            self.numbers = list(map(int, str(input("\nWrite numbers separated by comma: ")).split(',')))
            print("\nSample: {}".format(self.numbers))
            return self.numbers
        except ValueError:
            print("\nPlease, just integers numbers seperated by coma.")
            return self.manual_numbers()