import sys

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

    def start(self):
        while True:
            letter = str(input('Write a letter: '))
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