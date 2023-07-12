#!/usr/bin/python3
"""
7. Load, add, save

loads the list from add_item.json
adds arguments to the lists
and save it back to the json file
"""
from sys import argv
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


def load_from_json_file(filename):
    """
    Creates an object from a string

    Args:
        filename (str): name of the file

    Returns:
        object
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)


filename = "add_item.json"

try:
    data = load_from_json_file(filename)
except FileNotFoundError:
    data = []
data += argv[1:]
save_to_json_file(data, filename)
