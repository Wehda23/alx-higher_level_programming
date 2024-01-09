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
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value < 1:
            raise ValueError(f"{name} must be greater than 0")
