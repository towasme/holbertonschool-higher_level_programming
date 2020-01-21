#!/usr/bin/python3


class MyList(list):
    """
    Subclass Mylist that has a superclass named list
    """
    def print_sorted(self):
        """
        function that sorts and prints a list.
        """
        self.list = list
        print(sorted(self))
