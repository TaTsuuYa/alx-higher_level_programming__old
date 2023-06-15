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
    sp = 2
    split_rom = [roman_string[i: i + sp]
                 for i in range(0, len(roman_string), sp)]
    for i in split_rom:
        if len(i) != sp:
            n += rom[i[0]]
        else:
            if i[0] not in rom or i[1] not in rom:
                return 0

            if rom[i[0]] < rom[i[1]]:
                n += rom[i[1]] - rom[i[0]]
            else:
                n += rom[i[0]] + rom[i[1]]
    return n
