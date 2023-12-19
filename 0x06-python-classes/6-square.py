#!/usr/bin/python3
"""
This is a task made purposely for task 4
"""


class Square:
    """Class made for purpose to serve task 4"""
    def __init__(self, size=0, position=(0, 0)):
        """Adding Size to the class instance as private instance
        Args:
         - size: Size of a square.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if not (size >= 0):
            raise ValueError("size must be >= 0")

        if not all([isinstance(pa, int) and (pa >= 0) for pa in position]):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Property to retrieve position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method for changing value of position"""
        if not all([(isinstance(pa, int)) and (pa >= 0) for pa in value]):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """ Method used to print the square in # or nothing """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for row in range(self.__size):
                for column in range(self.__position[0]):
                    print(" ", end="")
                print("#" * self.__size)
