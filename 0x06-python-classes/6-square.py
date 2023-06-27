#!/usr/bin/python3
"""2. Size validation"""


class Square:
    """This is a square"""

    def __init__(self, size=0, position=(0, 0)):
        """initializing the square"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Gets the size value"""
        return self.__size

    @size.setter
    def size(self, size):
        """Sets the size value"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def position(self):
        """Gets the position value"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position value"""
        if not isinstance(value, tuple) or\
                not len(value) != 2 or\
                not all(isinstance(n, int) for n in value) or\
                not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """Prints the square in the right position"""
        if self.__size == 0:
            print()
            return

        print('\n' * self.__position[1], end='')
        for i in range(self.__size):
            print(' ' * self.__position[0] + '#' * self.__size)
