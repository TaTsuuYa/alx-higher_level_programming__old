#!/usr/bin/python3
"""
7. Load, add, save

loads the list from add_item.json
adds arguments to the lists
and save it back to the json file
"""

from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = \
    __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    data = load_from_json_file(filename)
except FileNotFoundError:
    data = []
data += argv[1:]
save_to_json_file(data, filename)
