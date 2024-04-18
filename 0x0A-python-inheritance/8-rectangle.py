#!/usr/bin/python3

"""Let's play with dimensions instead"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Don't reinvent the wheel, borrow some superpowers if you can"""

    def __init__(self, width, height):
        """Label things"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self._width = width
        self._height = height
