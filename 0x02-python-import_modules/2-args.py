#!/usr/bin/python3
from sys import argv
arg = len(argv) - 1
if arg == 0:
    print('0 arguments.')
elif arg == 1:
    print("{} argument:".format(arg))
elif arg > 1:
    print("{} arguments:".format(arg))
for i in range(arg):
    if arg != 0:
        print("{}: {}".format(i + 1, argv[i + 1]))
