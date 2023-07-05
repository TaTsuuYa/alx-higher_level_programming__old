#!/usr/bin/python3
"""
4. Text indentation
"""


def text_indentation(text):
    """
    Formats text

    Args:
        text (str): the text getting formatted
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    txt = ""
    i = 0
    while i < len(text):
        if text[i] in ".?:":
            txt += text[i] + '\n\n'
            if text[i + 1] == ' ':
                i += 1
        else:
            txt += text[i]
        i += 1
    print(txt, end='')
