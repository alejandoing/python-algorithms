import sys

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
                    pass
                elif method == 2: 
                    pass
                elif method == 3:
                    break
                elif method == 4:
                    sys.exit()
                else:
                    raise ValueError
                #self.get_standard_deviation(self.get_variance(self.numbers))

            except ValueError:
                print("\nCommand not found")
                continue