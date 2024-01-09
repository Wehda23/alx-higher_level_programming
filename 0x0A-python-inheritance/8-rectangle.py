#!/usr/bin/python3
"""
File contains class Called Geomtry
"""


class BaseGeometry:
    """
    Class For gemotric representations
    """
    def area(self):
        """Method that should calculate Area of Geometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Method that validates parameters

        Args:
            - name: Should of a python <str> type
            - value: Should be of python type <int>
        """
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")
        if value < 1:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    Two Dimensional Rectangular Shape Class
    """
    def __init__(self, width: int, height: int):
        """
        Intializing a new class instance

        Args:
            - width : Width of the rectangle as in integers
            - height: Height of the rectangle as in integers
        """
        # Validate integer
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height
