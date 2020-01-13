#!/usr/bin/python3


"""
say_my_name module:
function that prints the first and last name of a person
"""


def say_my_name(first_name, last_name=""):
    """
    Parameters:
        first_name: string containing the first name.
        last_name: string containing the last name.
    return:
        print whole name
    """
#    if first_name == None:
#        raise TypeError("first_name must be a string")
#    if last_name == None:
#        raise TypeError("last_name must be a string")
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

#    #print name and last name
    print("My name is {:s} {:s}".format(first_name, last_name))
