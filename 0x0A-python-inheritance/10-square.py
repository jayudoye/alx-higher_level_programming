
#!/usr/bin/python3

"""Let's make things even"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Squares are better that rectangles - no kidding :)
    """

    def __init__(self, size):
        self.integer_validator("size", size)
        self._size = size
        super().__init__(size, size)

    def area(self):
        """See?"""
        return self._size ** 2
