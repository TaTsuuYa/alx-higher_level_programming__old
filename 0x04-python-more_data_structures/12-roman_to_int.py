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
    for i in range(len(roman_string)):
        if roman_string[i] not in rom:
            return 0
        if i < len(roman_string) - 1:
            if roman_string[i] < roman_string[i + 1]:
                n += rom[roman_string[i + 1]] - rom[roman_string[i]]
                i += 1
            else:
                n += rom[roman_string[i]]
    return n


roman_number = "IIIX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
