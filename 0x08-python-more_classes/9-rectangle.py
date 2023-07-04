#!/usr/bin/python3
"""
9. A square is a rectangle
"""


class Rectangle:
    """
    This is a rectangle class

    Attributes:
        number_of_instances (int): number of current instances
        print_symbol (any): symbol for string representation
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initializing a Rectangle

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """

        self.width = width
        self.height = height

        self.increment_number_of_instances()

    @property
    def width(self):
        """Get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set width

        Raises:
            TypeError: if value is not an int
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set height

        Raises:
            TypeError: if value is not an int
            ValueError: if value is less than 0
        """
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
        """Increments the number of instances"""
        cls.number_of_instances += 1

    @classmethod
    def decrement_number_of_instances(cls):
        """Decrements the number of instances"""
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the biggest rectangle

        Args:
            rect_1 (Rectangle): rectangle object
            rect_2 (Rectangle): rectangle object
        Raises:
            TypeError: if either objects is not a Rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() < rect_2.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        """
        Returns a square

        Args:
            size (int): the width and height of the rectangle
        """
        return cls(size, size)
