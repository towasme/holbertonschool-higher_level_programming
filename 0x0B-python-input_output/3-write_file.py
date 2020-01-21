#!/usr/bin/python3
"""
function that reads a text file
"""


def write_file(filename="", text=""):
    with open(filename, 'w',  encoding='utf-8') as file:
        file.write(text)
    return len(text)
