#!/usr/bin/python3
"""
class Rectangle that inherits from class Base
"""

from models.base import Base

class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError(self.__width + "must be an integer width") #corregir salida nombre
        if value <= 0:
            raise ValueError("{} must be > 0".format(self.__width))
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer height".format(self.__height)) #corregir salida nombre
        if value <= 0:
            raise ValueError("{} must be > 0".format(self.__height))
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer") #corregir salida nombre
        if value < 0:
            raise ValueError("{} must be >= 0".format(self.__x))
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer y".format(self.__y)) #corregir salida
        if value < 0:
            raise ValueError("{} must be >= 0".format(self.__y))
        self.__y = value

    def area(self):
        return self.__width * self.__height

    def display(self):
        for o in range(self.__y):
            print()
        for i in range(self.__height):
            for j in range(self.__width):
                if j is 0:
                    print(" " * self.__x, end="")
                print("#", end="")
            print()

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)

