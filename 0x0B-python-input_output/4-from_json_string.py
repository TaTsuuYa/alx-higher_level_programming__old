#!/usr/bin/python3
"""4. From JSON string to Object"""
import json


def from_json_string(my_str):
    """
    Returns an object from @my_string

    Args:
        my_string (str): json string object

    Returns:
        object from json
    """
    return json.loads(my_str)
