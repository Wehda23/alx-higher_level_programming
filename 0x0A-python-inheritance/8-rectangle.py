#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry


"""
File contains class Called Geomtry
"""


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
