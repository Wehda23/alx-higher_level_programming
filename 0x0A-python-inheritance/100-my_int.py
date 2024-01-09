#!/usr/bin/python3

"""
File contains a MyInt Class
"""


class MyInt(int):
    """
    A Rebel class of int
    """
    def __eq__(self, other):
        return super().__ne__(other)
    
    def __ne__(self, other):
        return super().__eq__(other)
