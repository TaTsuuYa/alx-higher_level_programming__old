#!/usr/bin/python3
"""
7. Change representation
"""


class Rectangle:
    """This is a rectangle class"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

        self.increment_number_of_instances()

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

    @classmethod
    def increment_number_of_instances(cls):
        cls.number_of_instances += 1

    @classmethod
    def decrement_number_of_instances(cls):
        cls.number_of_instances -= 1

    def __str__(self):
        """Returns the rectangle as '#'s"""
        rec = ""
        if self.__height == 0 or self.__width == 0:
            return rec
        for y in range(self.__height):
            rec += (str(self.print_symbol) * self.__width) + \
                ('\n' if y < self.__height - 1 else '')
        return rec

    def __repr__(self):
        """Returns a string representation of this instance"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Bye, Bye"""
        print("Bye rectangle...")
        self.decrement_number_of_instances()
