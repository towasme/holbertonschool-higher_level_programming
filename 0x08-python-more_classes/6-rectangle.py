#!/usr/bin/python3
class Rectangle:
    """
    class Rectangle with two private attributes, width and height
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            return (self.__height + self.__width) * 2

    def __str__(self):
        str = ""
        if self.__width == 0 or self.__height == 0:
            return str
        else:
            for j in range(self.__height):
                for k in range(self.__width):
                    str += '#'
                str += '\n'
            str = str.rstrip()
            return str

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1 
