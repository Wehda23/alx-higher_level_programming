#!/usr/bin/python3
"""
This is a task made purposely for task 1
"""


class Square:
    """Class made for purpose to serve task 1"""
    def __init__(self, size=0):
        """Adding Size to the class instance as private instance
        Args:
         - size: Size of a square.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if not (size >= 0):
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        Public method used to return the area of the square based on size
        """
        return self.__size ** 2
