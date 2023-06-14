#!/usr/bin/python3

rom = {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}


def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    n = 0
    for i in roman_string:
        n += rom.get(i, 0)
    return n
