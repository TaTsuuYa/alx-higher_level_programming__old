#!/usr/bin/python3
"""2-is_same_class.py"""


def is_same_class(obj, a_class):
    """
    checks if obj is an instance of a_class
    """
    return obj.__class__.__name__ == a_class.__name__
