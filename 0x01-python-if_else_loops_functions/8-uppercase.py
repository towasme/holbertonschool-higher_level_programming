#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            y = ord(i) - 32
            print("{}".format(chr(y)), end="")
        else:
            print("{}".format(i), end="")
    print()
