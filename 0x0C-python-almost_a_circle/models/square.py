#!/usr/bin/python3
"""
new class square that inherits from Rectangle class
"""


from models.rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs): #corregir este codigo ya que no ejecuta bien
        if args is not None:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    @property
    def size(self):
        return (self.width)

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be > 0")
        self.width = value

    def to_dictionary(self):
        dicti = {}
        dicti['x'] = self.x
        dicti['y'] = self.y
        dicti['id'] = self.id
        dicti['size'] = self.size
        return (dicti)
