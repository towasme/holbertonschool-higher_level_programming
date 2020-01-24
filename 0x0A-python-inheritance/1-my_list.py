#!/usr/bin/python3


class MyList(list):

    def print_sorted(self):
        """
        function that sorts and prints a list.
        """
        print(sorted(self))
