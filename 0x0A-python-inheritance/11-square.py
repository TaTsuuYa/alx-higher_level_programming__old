#!/usr/bin/python3
"""11. Square #2"""


class BaseGeometry:
    """geo class with instance method area"""
    def area(self):
        """not implemented yet"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if value.__class__.__name__ != int.__name__:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """rectangle class"""
    def __init__(self, width, height):
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """calculate the area of the rectangle"""
        return self.__height * self.__width

    def __str__(self):
        return f"[{self.__class__.__name__}] {self.__width}/{self.__height}"


class Square(Rectangle):
    """a cube class"""
    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        return f"[{self.__class__.__name__}] {self.__size}/{self.__size}"
