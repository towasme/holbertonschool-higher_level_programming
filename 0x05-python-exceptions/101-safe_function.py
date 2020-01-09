#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except (IndexError, ZeroDivisionError, TypeError, ValueError) as error:
        sys.stderr.write("Exception: {}\n".format(error))
        return None
