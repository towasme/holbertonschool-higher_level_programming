#!/usr/bin/python3
class MyList(list):
    """
    Subclass Mylist that has a superclass named list
    """
    def print_sorted(self):
        self.list = list
        """
        function that sorts and prints a list.
        """
        print(sorted(self))
