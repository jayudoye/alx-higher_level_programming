#!/usr/bin/python3
"""Square class definition"""


class Square:
    """Square class definition with attribute size"""

    def __init__(self, size=0):
        """Initializer"""

        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Public instance method that returns the current square area"""
        return self.__size * self.__size

    @property
    def size(self):
        """Retrieve private instance attribute size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Property setter to change the value of size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
