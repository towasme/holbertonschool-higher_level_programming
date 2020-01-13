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

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not int:
        raise TypeError("b must be an integer")
#    if type(b) is tuple or type(b) is list or type(b) is str \
#            or type(b) is set:
#        raise TypeError("b must be an integer")
    return (a + b)
