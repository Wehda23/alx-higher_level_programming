#!/usr/bin/python3

""" File that contains class Base """

class Base:
    """
    The goal of it is to manage id attribute in all my
    future classes and to avoid duplicating the same code
    by (extrension, same bugs)
    
    Private class Attributes:
        - __nb_objects: is a private class attribute represents\
                number of objects created from this class
    """

    __nb_objects: int = 0

    def __init__(self, id= None):
        """
        Initiating class instance

        Args:
            - id: Id of the instance
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects