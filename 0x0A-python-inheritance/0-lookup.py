#!/usr/bin/python3
"""0. Lookup"""


def lookup(obj):
    """
    Returns a list of object attributes and methods.

    Args:
        obj (object): the object which attributes gets returned
    """
    return dir(obj)
