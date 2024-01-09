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
        """Initiating new instance"""
        # Validate width
        self.integer_validator("width", width)
        self.__width = width
        # Validate height
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the area of the rectangle"""
        return self.__height * self.__width

    def __str__(self):
        """String of object"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """
    class called Square
    """
    def __init__(self, size):
        """Initialize new instance of class"""
        # Validate size
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Calculates the area of square"""
        return self.__size ** 2
