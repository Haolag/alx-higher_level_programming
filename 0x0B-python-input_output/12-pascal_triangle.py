#!/usr/bin/python3
"""
12-pascal_triangle.py
Create a function def pascal_triangle(n): that returns
a list of lists of integers representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """
    returns pascal triangle of n.
    """

    if n <= 0:
        return []

    limit = n - 1
    triangle = [[1]]

    for i in range(limit):
        row = []
        row.append(1)

        if len(triangle[i]) > 1:
            prev_row_len = len(triangle[i]) - 1
            nxt = 1

            for j in range(prev_row_len):
                suma = triangle[i][j] + triangle[i][nxt]
                row.append(suma)
                nxt += 1

        row.append(1)
        triangle.append(row)

    return triangle
