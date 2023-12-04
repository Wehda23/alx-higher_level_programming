#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for array in matrix:
        for number, element in enumerate(array, start=1):
            if number == len(array):
                print("{:d}".format(element), end="")
            else:
                print("{:d} ".format(element), end='')
        print("")
