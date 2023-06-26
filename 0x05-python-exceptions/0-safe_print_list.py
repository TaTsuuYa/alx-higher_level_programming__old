#!/usr/bin/bash


def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print(my_list[i], end='')
    except:
        pass
    print()
 