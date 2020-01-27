#!/usr/bin/python3
"""
new class square that inherits from Rectangle class
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Class square that inherits from Rectangle"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """overrides the string to return a specific message"""
        return "[Square] ({}) {}/{} - {}" \
            .format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'size':
                    self.size = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    @property
    def size(self):
        """size getter"""
        return (self.width)

    @size.setter
    def size(self, value):
        """size setter"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be > 0")
        self.width = value

    def to_dictionary(self):
        """returns a dictionary withh  the attributes of the class"""
        dicti = {}
        dicti['x'] = self.x
        dicti['y'] = self.y
        dicti['id'] = self.id
        dicti['size'] = self.size
        return (dicti)
