#!/usr/bin/python3

"""
File contains class Called Student
"""


class Student:
    """
    Class Represents A Student
    """

    def __init__(self, first_name, last_name, age):
        """
        Class Initiation
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None) -> dict:
        """Method Retrieves Dictionary Representation"""
        data: dict = vars(self)

        if attrs and isinstance(attrs, list):
            data: dict = {
                    key: value for key, value in data.items()
                    if key in attrs
            }

        return data
