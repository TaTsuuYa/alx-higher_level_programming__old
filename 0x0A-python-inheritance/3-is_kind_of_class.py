#!/usr/bin/python3
"""3. Same class or inherit from"""


def is_kind_of_class(obj, a_class):
    """checks if obj is a direct/indirect subclass of a_class"""
    return isinstance(obj, a_class)
