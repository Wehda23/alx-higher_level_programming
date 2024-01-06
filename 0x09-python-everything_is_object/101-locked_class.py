#!/usr/bin/python3


"""
File contains LockedClass
"""


class LockedClass:
    """Locked Class"""
    def __setattr__(self, name, value):
        """Method used"""
        error: str = "'LockedClass' object has no attribute '{}'".format(name)
        if name != 'first_name':
            raise AttributeError(error)
        else:
            super().__setattr__(name, value)
