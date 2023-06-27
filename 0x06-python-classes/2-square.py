#!/usr/bin/python3
"""2. Size validation"""


class Square:
    """This is a square"""

    def __init__(self, size=0):
        """initializing the square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
