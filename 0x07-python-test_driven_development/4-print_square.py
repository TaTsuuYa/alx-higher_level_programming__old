#!/usr/bin/python3
"""
3. Print square
"""


def print_square(size):
    """
    Prints a square

    Args:
        size (int): size of the square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if size != 0:
        rec = ""
        for y in range(size):
            rec += ("#" * size) + ('\n' if y < size - 1 else '')
        print(rec)
