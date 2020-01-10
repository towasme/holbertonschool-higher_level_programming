#!/usr/bin/python3
import dis


class MagicClass:
    """class Square with a private attribute called size"""
    def __init__(self, radius=0):
        if (type(radius) is not int) or type(radius) is not float:
            raise TypeError('radius must be a number')
        return self.radius

print(dis.dis(MagicClass))
