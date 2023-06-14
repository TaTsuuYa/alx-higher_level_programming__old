#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary: dict) -> None:
    dic: dict = dict(sorted(a_dictionary.items()))
    for k, e in dic.items():
        print("{}: {}".format(k, e))
