#!/usr/bin/python3
"""
superclass BaseGeometry
"""


class BaseGeometry:
    """
    class base geometry with a instance method area
    """
    def area(self):
        """
        returns the area of a figure.
        """
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
        BaseGeometry().integer_validator("width", width)
        BaseGeometry().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        returns the area of a figure
        """
        return self.__size * self.__size

    def __str__(self):
        """
        informal way of writing a rectangle
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def __repr__(self):
        """
        formal way of writing a rectangle
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

class Square(Rectangle):
    """
    sub class that inherits from Rectangle
    """
    def __init__(self, size):
        """
        initialize instances
        """
        self.__size = size
        BaseGeometry().integer_validator("size", size)
        Rectangle.area(size)
