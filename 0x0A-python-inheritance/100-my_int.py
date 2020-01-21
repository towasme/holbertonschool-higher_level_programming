#!/usr/bin/python3
class MyInt(int):
    def __init__(self, x):
        self.x = x

    def __eq__(self, other):
        return isinstance(other, MyInt) and self.x == other.x

    def __ne__(self, other):
        return not self.__eq__(other)
