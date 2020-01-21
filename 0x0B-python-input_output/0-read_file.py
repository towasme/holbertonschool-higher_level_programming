#!/usr/bin/python3
"""
function that reads a text file
"""


def read_file(filename=""):
    with open(filename, encoding='utf-8') as file:
        read_data = file.read()
        print(read_data, end="")
