#!/usr/bin/python3
"""
function that append to a line
"""


def append_write(filename="", text=""):
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text)
    return len(text)
