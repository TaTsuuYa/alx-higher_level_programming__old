#!/usr/bin/python3

def uniq_add(my_list=[]):
    lst = list(set(my_list))
    sum = 0
    for x in lst:
        sum += x
    return sum
