#!/usr/bin/python3
"""1. My list"""


class MyList(list):
    """custom list class"""
    def print_sorted(self):
        print(sorted(self))
