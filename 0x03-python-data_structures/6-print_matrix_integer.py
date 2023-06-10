#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        return None
    for lst in matrix:
        lstlen = len(lst)
        for i in range(lstlen):
            if i < lstlen - 1:
                print("{:d}".format(lst[i]), end=' ')
            else:
                print("{:d}".format(lst[i]))
