#!/usr/bin/python3
"""
Create a function def pascal_triangle(n): that returns a list of lists of
integers representing the Pascal’s triangle of n:

Returns an empty list if n <= 0
You can assume n will be always an integer
You are not allowed to import any module
"""


def pascal_triangle(n):
    """Returns a pascal triangle of size n"""
    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    res = [[1], [1, 1]]

    for i in range(2, n):
        row = [1]
        prev = res[i - 1]
        for j in range(len(prev) - 1):
            row.append(prev[j] + prev[j + 1])
        row.append(1)
        res.append(row)

    return res
