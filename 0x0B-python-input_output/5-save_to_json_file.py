#!/usr/bin/python3
"""5. Save Object to a file"""
import json


def save_to_json_file(my_obj, filename):
    """
    Saves an object to a file

    Args:
        my_obj (object): the saved object
        filename (str)L name of the file
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
