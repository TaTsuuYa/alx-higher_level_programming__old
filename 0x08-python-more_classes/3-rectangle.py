#!/usr/bin/python3
"""
3. String representation
"""


class Rectangle:
    """This is a rectangle class"""

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of the instance"""
        return self.__height * self.__width

    def perimeter(self):
        """Calculated the perimeter of this instance"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        """Returns the rectangle as '#'s"""
        rec = ""
        if self.__height == 0 or self.__width == 0:
            return rec
        for y in range(self.__height):
            rec += ("#" * self.__width) + \
                ('\n' if y < self.__height - 1 else '')
        return rec
