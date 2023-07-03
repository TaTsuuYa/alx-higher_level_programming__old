#!/usr/bin/python3
"""
0. Integers addition
"""


def add_integer(a, b=98):
    """
    Adds two integers

    Args:
        a (int): first number
        b (int): second number
    """

    if not isinstance(a, int):
        raise TypeError("a must be an integer")

    if not isinstance(b, int):
        raise TypeError("b must be an integer")

    return a + b
