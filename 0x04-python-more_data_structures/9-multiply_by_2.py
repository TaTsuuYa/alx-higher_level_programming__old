#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    dic = a_dictionary.copy()
    for k, e in dic.items():
        dic[k] = e * 2
    return dic
