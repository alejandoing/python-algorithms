import sys

class FibonacciSequence:
    def __init__(self):
        print('''
            ____________________________________________
            ______ _ _                                _ 
            |  ___(_) |                              (_)
            | |_   _| |__   ___  _ __   __ _  ___ ___ _ 
            |  _| | | '_ \ / _ \| '_ \ / _` |/ __/ __| |
            | |   | | |_) | (_) | | | | (_| | (_| (__| |
            \_|   |_|_.__/ \___/|_| |_|\__,_|\___\___|_|
            ____________________________________________                                           
        ''')
    
    def start(self):
        while True:
            
            print(''' 
                Select a option:

                [1]: Look for a number by it's index
                [2]: Write sequence until
                [3]: Back to main menu
                [4]: Exit
            ''')

            try:
                method = int(input("\nYour option: "))
                if method == 1:
                    self.look_by_index()
                elif method == 2: 
                    self.write_sequence()
                elif method == 3:
                    break
                elif method == 4:
                    sys.exit()
                else:
                    raise ValueError

            except ValueError:
                print("\nCommand not found")
                continue

    def look_by_index(self):
        pass
    
    def write_sequence(self):
        limit = 200
        sequence = [0, 1]
        print("0: 0")
        for position in range(1, limit + 1):
            print("{}: {}".format(position, sequence[-1]))
            sequence = [sequence[1], sequence[0] + sequence[1]]