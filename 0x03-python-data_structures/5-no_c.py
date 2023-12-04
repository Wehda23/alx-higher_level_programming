#!/usr/bin/python3
def no_c(my_string):
    string = "".join([char for char in my_string if char not in ['c', 'C']])
    return string
