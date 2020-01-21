#!/usr/bin/python3
"""
Fucntions that checks if objet is an instance from a superclass
"""


def inherits_from(obj, a_class):
    """
    return true if its a inherited object ir fals if it isnt't
    """
    if (isinstance(obj, a_class)) and (a_class is not type(obj)):
        return True
    else:
        return False
