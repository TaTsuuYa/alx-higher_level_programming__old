#!/usr/bin/python3

def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= ord('a') and ord(str[i]) <= ord('z'):
            s = chr(ord(str[i]) + (ord('a') - ord('A')))
        else:
            s = str[i]
        print("{}".format(s), end='')
    print()
