#!/usr/bin/python3
def uppercase(str):
    for i in str:
        j = ord(i)
        if j >= 97 and j <= 122:
            j = j - 32
        print("{}".format(chr(j)), end="")
    print()
