#!/usr/bin/python3


"""
add integers:
Function that adds two integers or floats
"""


def add_integer(a, b=98):
    """
    Parameters:
        a: integer
        b: integer
    Return:
        the sum of the two numbers
    """

    if a is None:
        raise TypeError("a must be a integer")
    if b is None:
        raise TypeError("b must be a integer")
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(a) is not float:
        raise TypeError("b must be an integer")
    if type(b) is tuple or type(b) is list or type(b) is str \
            or type(b) is set:
        raise TypeError("b must be an integer")
    return int(a + b)
