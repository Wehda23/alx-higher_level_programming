#!/usr/bin/python3

"""
File that contains a class called Rectangle
"""


class Rectangle:
    """Class Two Dimensional (2D) Rectangle"""

    def __init__(self, width: int = 0, height: int = 0):
        """
        Initiate private instance attributes

        Args:
            - width: width of the triangle in form of python integer.
            - height: height of the triangle in form of python integer.
        """
        self._set_width(width)
        self._set_height(height)

    def _set_width(self, width: int) -> None:
        """
        Method used to set the width of the rectangle

        Args:
            - value: Is an integer value that is going to be set\
                    or ovewrites the current width of rectangle.
        Returns:
            - Nothing.
        """
        # Check the type of the input
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        # Check the value of the input
        if width < 0:
            raise ValueError("width must be >= 0")
        # Set the new width
        self.__width: int = width

    def _set_height(self, height: int) -> None:
        """
        Method used to set a new value for height of the rectangle.

        Args:
            - value: Is an integer value that is going to be set as new value\
                    of height of the rectangle.

        Returns:
            - Nothing.
        """
        # Check the type of input
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        # Check value of the input
        if height < 0:
            raise ValueError("height must be >= 0")
        # Set the new height
        self.__height: int = height

    @property
    def width(self) -> int:
        """Property Used to return the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value: int) -> None:
        """Property Setter for the width of the rectangle"""
        self._set_width(value)

    @property
    def height(self) -> int:
        """Property used to return the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value) -> None:
        """
        Property Setter used to set a new value to the height of the rectangle

        Args:
            - value: A new value to set to the height of the rectangle.
        """
        self._set_height(value)

    def area(self) -> int:
        """Public method used to return area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self) -> int:
        """Public method used to return the perimeter of the rectangle"""
        # Grab the height and width of the rectangle
        width: int = self.__width if self.__height > 0 else 0
        height: int = self.__height if self.__width > 0 else 0

        # Return the parameter
        return 2 * (width + height)
