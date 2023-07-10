#!/usr/bin/python3


def lookup(obj: object):
    """
    Returns a list of object attributes and methods.

    Args:
        obj (object): the object which attributes gets returned
    """
    return dir(obj)
