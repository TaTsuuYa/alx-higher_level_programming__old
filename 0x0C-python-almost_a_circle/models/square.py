#!/usr/bin/python3
"""
10. And now, the Square!,
11. Square size,
12. Square update,
14. Square instance to dictionary representation
"""
from rectangle import Rectangle


class Square(Rectangle):
    """
    Square class inheriting from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, val):
        self.width = val
        self.height = val

    def __str__(self):
        """defining the string"""
        return f"[{self.__class__.__name__}] ({self.id})"\
            f" {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """Updating this instance's attributes"""
        attrs = ["id", "size", "x", "y"]
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
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
