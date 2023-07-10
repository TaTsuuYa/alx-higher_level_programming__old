#!/usr/bin/python3
"""4. Only sub class of"""


def inherits_from(obj, a_class):
    """checks if obj inherits directly or indirectly from a_class"""
    return obj.__class__.__name__ != a_class.__name__ and\
        isinstance(obj, a_class)
