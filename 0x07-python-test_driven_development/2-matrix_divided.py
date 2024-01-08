#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Function that divides all elements of a matrix

    Args:
        - matrix: must be a list of integer or float otherwise an error\
                will be raised, also rows must be equal..
        - div: Must be an integer number or float otherwise an error\
                will be raised and can't be equal to 0 will raise\
                ZeroDivsionError
    
    Returns:
        New matrix
    """
    length: int = len(matrix[0])
    # Check if it is all int or float
    for row in matrix:
        if isinstance(row, list):
            if len(row) != length:
                raise TypeError("Each row of the matrix must have the same size")
            for number in row:
                if not isinstance(number, (int, float)):
                    raise TypeError("matrix must be (list of lists) of integers/floats")
        else:
            raise TypeError("matrix must be (list of lists) of integers/floats")
    
    # Check div
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(element / div, 2) for element in row] for row in matrix]

    return new_matrix
