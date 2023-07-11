#!/usr/bin/python3
"""0. Read file"""


def read_file(filename=""):
    """Prints a filename."""
    with open(filename, encoding="utf-8") as file:
        print(file.read())
