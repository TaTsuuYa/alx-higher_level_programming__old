#!/usr/bin/python3

def print_last_digit(number):
    if number < 0:
        number = -number
    r = number % 10
    print(f"{r}", end='')
    return r
