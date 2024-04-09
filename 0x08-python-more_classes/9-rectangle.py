#!/usr/bin/python3

"""An empty rectangle class"""

print("__name__ is", __name__)

class Rectangle:
    """Rectangle blueprint"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ Initializer """
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Computes area """
        return self.width * self.height

    def perimeter(self):
        """ Computes perimeter """
        if self.width == 0 or self.height == 0:
            return 0
        return self.width * 2 + self.height * 2

    def __str__(self):
        """Returns a string representation of self"""
        if self.width == 0 or self.height == 0:
            return ""
        res = ""
        for i in range(self.height):
            res += str(self.print_symbol) * self.width
            if i < self.height - 1:
                res += '\n'
        return res

    def __del__(self):
        """On delete hook"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def __gt__(self, other):
        """Checks whether self is greater than other"""
        return self.area() > other.area()

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares rectangle instances"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return max(rect_1, rect_2)

    @classmethod
    def square(cls, size=0):
        """Creates a square (a rectangle with equal width and height)"""
        sq = Rectangle(size, size)
        return sq
