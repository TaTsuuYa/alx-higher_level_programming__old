#!/usr/bin/python3
"""
2. Say my name
"""


def print_square(size):
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    rec = ""
    for y in range(size):
        rec += ("#" * size) + ('\n' if y < size - 1 else '')
    print(rec)
