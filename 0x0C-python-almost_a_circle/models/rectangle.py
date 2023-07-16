#!/usr/bin/python3
"""
2. First Rectangle,
3. Validate attributes,
4. Area first,
5. Display #0,
6. __str__,
7. Display #1,
8. Update #0,
9. Update #1,
13. Rectangle instance to dictionary representation
"""
from base import Base


class Rectangle(Base):
    """
    Rectangle class inheriting from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, val):
        self.not_int(val, "width")
        self.lt_0(val, "width")
        self._width = val

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, val):
        self.not_int(val, "height")
        self.lt_0(val, "height")
        self._height = val

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, val):
        self.not_int(val, "x")
        self.le_0(val, "x")
        self._x = val

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, val):
        self.not_int(val, "y")
        self.le_0(val, "y")
        self._y = val

    def area(self):
        """Calculates the area"""
        return self.width * self.height

    def display(self):
        """Prints the instance with '#' symbol"""

        # handling y
        [print() for i in range(self.y)]
        for i in range(self._height):
            [print(" ", end="") for i in range(self.x)]
            print('#' * self.width)

    def __str__(self):
        """defining the string"""
        return f"[{self.__class__.__name__}] ({self.id})"\
            f" {self.x}/{self.y} - "\
            f"{self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """Updating this instance's attributes"""
        attrs = ["id", "width", "height", "x", "y"]
        # handling args
        args_len = len(args)
        if args_len > 0:
            for i in range(args_len):
                setattr(self, attrs[i], args[i])
            return
        # handling kwargs
        for attr in attrs:
            val = kwargs.get(attr, None)
            if val is not None:
                setattr(self, attr, val)

    def to_dictionary(self):
        """
        Converts to dictionary
        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    # tools
    def not_int(self, obj, attr_name):
        """Checks whether an attribute is an integer"""
        if type(obj) is not int:
            raise TypeError(f"{attr_name} must be an integer")

    def lt_0(self, obj, attr_name):
        """Checks whether an attribute is greater than 0"""
        if obj <= 0:
            raise ValueError(f"{attr_name} must be > 0")

    def le_0(self, obj, attr_name):
        """Checks whether an attribute is greater than or equal to 0"""
        if obj < 0:
            raise ValueError(f"{attr_name} must be >= 0")
