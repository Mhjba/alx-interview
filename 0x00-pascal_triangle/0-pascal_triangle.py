#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing Pascal's triangle up to level n."""
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        k = [1]

        for j in range(1, i):
            k.append(triangle[i-1][j-1] + triangle[i-1][j])
        k.append(1)
        triangle.append(k)

    return triangle
