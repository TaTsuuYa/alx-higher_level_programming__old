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
        if i not in rom:
            return 0
        n += rom[i]
    return n


roman_number = "IIIX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
