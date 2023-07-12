#!/usr/bin/python3
"""12. Pascal's Triangle"""


def pascal_triangle(n):
    """
    Returns pascals triangle

    Args:
        n (int): triangle hight

    Returns:
        (list) a matrix containing the pascal triangle of n
    """
    if n <= 0:
        return []

    pas = [[1] * x for x in range(1, n + 1)]
    for i, lst in enumerate(pas):
        for j, num in enumerate(lst):
            try:
                x = i - 1
                y = j - 1
                if x < 0 or y < 0:
                    continue
                pas[i][j] = pas[x][j] + pas[x][y]
            except IndexError:
                pass
    return pas
