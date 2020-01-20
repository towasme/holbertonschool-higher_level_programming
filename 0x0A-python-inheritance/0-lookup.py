#!/usr/bin/python3
def lookup(obj):
    """
    Function return a list with all the methods and attributes of an object
    @obj: object to retrieve
    return a list
    """
    return dir(obj)
