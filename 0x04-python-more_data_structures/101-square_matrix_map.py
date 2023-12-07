#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda array: list(map(lambda n: n**2, array)), matrix))
