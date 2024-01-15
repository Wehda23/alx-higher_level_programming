#!/usr/bin/python3

"""
File that contains class called Base
"""


class Base:
    """
    The goal of class base is to manage
    id attribute in all the future classes to avoid
    duplicating the same code (by extension, same bugs).

    Attributes:
        - __nb_objects: is a private class attribute represents\
                number of objects created from this class
    """
    __nb_objects: int = 0

    def __init__(self, id=None):
        """
        Class initiation of public instances

        Args:
            id: Public class instance attribute
        """
        if not id:
            # Increment instance number of objects.
            Base.__nb_objects += 1
            self.id: int = self.__nb_objects
        else:
            self.id = id
