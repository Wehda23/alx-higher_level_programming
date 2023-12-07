#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda array: [num**2 for num in array], matrix))
