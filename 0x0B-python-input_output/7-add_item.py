#!/usr/bin/python3
"""7. Load, add, save"""
from sys import argv
import json

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "add_item.json"

with open(filename, 'w', encoding="utf-8") as f:
    json.dump(argv[1:], f)
