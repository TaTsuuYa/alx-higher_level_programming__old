#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    lst = []
    for i in my_list:
        if i != idx:
            lst.append[i]
    my_list = lst
    return lst
