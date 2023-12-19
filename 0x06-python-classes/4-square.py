#!/usr/bin/python3
"""
This is a task made purposely for task 4
"""


class Square:
    """Class made for purpose to serve task 4"""
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

    @property
    def size(self):
        """Proptery to retrieve size """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter function the set a new value for size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if not (value >= 0):
            raise ValueError("size must be >= 0")
        self.__size = value
