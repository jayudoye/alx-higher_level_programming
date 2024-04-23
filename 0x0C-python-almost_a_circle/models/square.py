#!/usr/bin/python3

"""
A square class
"""

from .rectangle import Rectangle


class Square(Rectangle):
    """Square class derived from Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return """[Square] ({}) {}/{} - {}""".format(
                self.id, self.x, self.y, self.width)

        @property
    def size(self):
        """Gets the size aka width of self"""
        return self.width

    @size.setter
    def size(self, value):
        """Updates the width and height of self"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update properties based on args and kwargs
        :param args: (id, size, x and y) respectively
        :param kwargs: an optional dictionary containing the keys (id,
         size, x and y) whose values are used to update the
         attributes of self
        """
        for i in range(min(len(args), 4)):
            arg = args[i]
            if i == 0:
                self.id = arg
            elif i == 1:
                self.size = arg
            elif i == 2:
                self.x = arg
            else:
                self.y = arg
        if not args and kwargs:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """Returns the dictionary representation of self"""
        keys = ['id', 'x', 'size', 'y']
        return {k: getattr(self, k) for k in keys}
