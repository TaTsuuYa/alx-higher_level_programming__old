#!/usr/bin/python3
"""1. Write to a file"""


def write_file(filename="", text=""):
    """
    Prints @text to @filename.

    Args:
        filename (str): name of the file
        text (str): text written
    """
    with open(filename, 'w', encoding="utf-8") as file:
        return file.write(text)
