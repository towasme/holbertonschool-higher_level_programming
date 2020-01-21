#!/usr/bin/python3
"""
empty class
"""


class BaseGeometry:
    """
    class base geometry with a instance method area
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """
    class inheriated from BaseGeometry
    """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        BaseGeometry().integer_validator("width", width)
        BaseGeometry().integer_validator("height", height)
