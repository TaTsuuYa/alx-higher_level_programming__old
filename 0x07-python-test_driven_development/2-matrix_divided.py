#!/usr/bin/python3
"""
1. Divide a matrix
"""


def matrix_divided(matrix, div):
    """
    divide a matrix elements by a number

    Args:
        matrix (list of lists): a matrix
        div (int or float): divisor
    Raises:
        TypeError: if div is not a number
            or matrix is not a list of lists of numbers
            or the lists inside matrix are of different sizes
        ZeroDivisionError: if div is zero
    """

    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    for lst in matrix:
        if not isinstance(lst, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        for n in lst:
            if not (isinstance(n, int) or isinstance(n, float)):
                raise TypeError("matrix must be a matrix "
                                "(list of lists) of integers/floats")

    for lst in range(len(matrix) - 1):
        if len(matrix[lst]) != len(matrix[lst + 1]):
            raise TypeError("Each row of the matrix must have the same size")

    mat = []
    for lst in matrix:
        new_lst = []
        for n in lst:
            new_lst.append(round(n / div, 2))
        mat.append(new_lst)

    return mat
