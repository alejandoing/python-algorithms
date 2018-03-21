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
                    index = int(input("\nWrite a number: "))
                    number = self.look_by_index(index)
                    print("\nThe number {} in the Fibonacci Sequence is {}".format(index, number))
                elif method == 2:
                    limit = int(input("\nSet the limit: "))
                    self.write_sequence(limit)
                elif method == 3:
                    break
                elif method == 4:
                    sys.exit()
                else:
                    raise ValueError

            except ValueError:
                print("\nCommand not found")
                continue

    def look_by_index(self, index):
        sequence = [0, 1]
        if not index:
            return 0
        for position in range(1, index):
            sequence = [sequence[1], sum(sequence)]
        return sequence[-1]
    
    def write_sequence(self, limit):
        sequence = [0, 1]
        print("0: 0")
        for position in range(1, limit + 1):
            print("{}: {}".format(position, sequence[-1]))
            sequence = [sequence[-1], sum(sequence)]