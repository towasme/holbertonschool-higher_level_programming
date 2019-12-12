#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    arg = len(argv) - 1
    c = 0
    if arg == 0:
        print('0')
    elif arg == 1:
        print(int(argv[1]))
    elif arg > 1:
        for i in range(arg):
            c += int(argv[i + 1])
        print("{}".format(c))
