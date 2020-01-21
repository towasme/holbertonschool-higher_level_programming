#!/usr/bin/python3
"""
function that returns true if the object is
exactly and instance of the specified class
    return: True or False
"""


def is_same_class(obj, a_class):
    """
    checks for a specific instance
    @obj: the object to check
    @a_class: the specified class
    returns: true if its an instance or false if not an instance
    """
    result = issubclass(a_class, type(obj))
    if result:
        return True
    else:
        return False
