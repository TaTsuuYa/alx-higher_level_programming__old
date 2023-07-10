#!/usr/bin/python3
"""7. Integer validator"""


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
