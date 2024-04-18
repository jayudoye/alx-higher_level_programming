#!/usr/bin/python3
"""A class that raises an Exception message"""


class BaseGeometry:
    """The BaseGeometry class"""

    def area(self):
        """To raise an Exception message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method that validates value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
