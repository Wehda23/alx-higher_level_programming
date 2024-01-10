#!/usr/bin/python3

"""
File COOL pascale triangle function
"""


def pascal_triangle(n):
    """
    returns a pascal triangle array
    """

    if n <= 0:
        return []

    triangle: list[list[int]] = [[1]]

    # Iterate over the rows
    for row in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]

        # Iterate over the row
        for i in range(1, row):
            new_row.append(prev_row[i - 1] + prev_row[i])

        new_row.append(1)
        triangle.append(new_row)

    return triangle
