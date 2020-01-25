#!/usr/bin/python3
"""
function that reads a text file
"""


def read_lines(filename="", nb_lines=0):
    with open(filename, encoding='utf-8') as file:
        long = len(file.readline())

    if nb_lines <= 0 or nb_lines >= long:
        with open(filename, encoding='utf-8') as file:
            read_data = file.read()
            print(read_data, end="")
    else:
        with open(filename, encoding='utf-8') as file:
            for j in range(nb_lines):
                print(file.readline(), end="")
