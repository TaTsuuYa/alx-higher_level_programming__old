#!/usr/bin/python3
"""2. Append to a file"""


def append_write(filename="", text=""):
    """
    Appends @text to @filename.

    Args:
        filename (str): name of the file
        text (str): text appended
    """
    with open(filename, 'a', encoding="utf-8") as file:
        return file.write(text)
