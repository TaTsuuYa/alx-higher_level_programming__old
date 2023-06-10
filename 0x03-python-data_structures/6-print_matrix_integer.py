#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for lst in matrix:
        lstlen = len(lst)
        for i in range(lstlen):
            if i < lstlen - 1:
                print("{}".format(lst[i]), end=' ')
            else:
                print("{}".format(lst[i]))
