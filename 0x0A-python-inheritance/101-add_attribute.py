#!/usr/bin/python3

"""
File that contains an awsome function
"""


def add_attribute(obj, attr_name, attr_value):
    """
    Function that addes new attribute to an object
    """
    if hasattr(obj, '__dict__'):
        obj.__dict__[attr_name] = attr_value
    else:
        raise TypeError("can't add new attribute")
