#!/usr/bin/python3
"""3. To JSON string"""
import json


def to_json_string(my_obj):
    """
    Returns the string rep of @my_obj

    Args:
        my_obj (object): my_obj
    """
    return json.dumps(my_obj)
