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
        """Method to validate value"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value < 1:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    Class representeds a 2D Geometry
    """
    def __init__(self, width, height):

        # Validate width
        self.integer_validator("width", width)
        self.__width = width
        # Validate height
        self.integer_validator("height", height)
        self.__height = height
