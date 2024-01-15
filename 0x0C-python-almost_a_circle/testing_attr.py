#!/usr/bin/python3


"""
File to test instance attribute
"""

from models.rectangle import Rectangle



test: Rectangle = Rectangle(10, 20, 15, 9)

test.to_dictionary()
