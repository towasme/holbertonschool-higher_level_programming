#!/usr/bin/python3
"""
funct that counts the number of lines
"""


def number_of_lines(filename=""):
    cont = 0
    with open(filename, encoding='utf-8') as file:
        for i in file:
            cont += 1
        return cont                 
