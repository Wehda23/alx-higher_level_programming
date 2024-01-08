#!/usr/bin/python3
"""
File that contains function that checks instance of class
"""


def is_same_class(obj, a_class) -> bool:
    """
    function that checks instance of a class
    """
    return type(obj) is a_class
