#!/usr/bin/python3
"""
File contains function called
inherits_from
"""


def inherits_from(obj, a_class):
    """
    Inherits directly or indirectly from class
    """
    return False if type(obj) is a_class else isinstance(obj, a_class)
