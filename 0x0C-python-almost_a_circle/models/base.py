#!/usr/bin/python3

"""
File that contains class called Base
"""

import json


class Base:
    """
    The goal of class base is to manage
    id attribute in all the future classes to avoid
    duplicating the same code (by extension, same bugs).

    Attributes:
        - __nb_objects: is a private class attribute represents\
                number of objects created from this class
    """
    __nb_objects: int = 0

    def __init__(self, id=None):
        """
        Class initiation of public instances

        Args:
            id: Public class instance attribute
        """
        if not id:
            # Increment instance number of objects.
            Base.__nb_objects += 1
            self.id: int = self.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries: list[dict]):
        """
        Static Method used to return json

        Returns:
             Json Object
        """
        if list_dictionaries:
            return json.dumps(list_dictionaries)

        return json.dumps("[]")

    @classmethod
    def save_to_file(cls, list_objs: list) -> None:
        """
        Class Method used to write JSON string to a file

        Args:
            - list_objs: list of Base instances or subclass instnaces
        """
        # Check if not none
        if list_objs is None:
            list_objs: list = []

        file_name: str = f"{cls.__name__}" + ".json"
        json_string: str = cls.to_json_string(
                [obj.to_dictionary() for obj in list_objs]
        )

        with open(file_name, mode='w', encoding='utf-8') as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string: str) -> list:
        """
        Static method used to convert json to Python objects

        Returns:
            - Python Object in <list>
        """
        # If json_string is none or empty
        if not json_string or json_string == "":
            # Return empty python list
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Class Method used to return instances with all attributes
        already set.

        Args:
            - **dictionary: Attributes of the new instance
        """
        # Check dict
        if dictionary:
            if cls.__name__ == "Rectangle":
                # Create new instance of rectangle
                new_instance = cls(1, 1)
            else:
                # Square class
                new_instance = cls(1)
            # Update using the Dictionary
            new_instance.update(**dictionary)
            # Return the new instance
            return new_instance

    @classmethod
    def load_from_file(cls) -> list:
        """
        Reads .json file data and return as python list

        Returns:
            - Python list that contains data
        """
        # Read the data
        file_name: str = cls.__name__ + ".json"
        # Check if file exists or not.
        try:
            with open(file_name, mode='r', encoding='utf-8') as file:
                # Read the file
                data: str = file.read()
                # Convert back to python dictionaries
                json_string: list = cls.from_json_string(data)
                # Create instances and store in a list
                instances: list = [cls.create(**obj) for obj in json_string]
                # Return the list
                return instances
            # File does not exist just return an empty list
        except Exception as e:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs) -> None:
        """
        Class Method used to save to .csv file

        Args:
            - list_objs: list that contains different instance objects
        """
        # First step we will use .to_dictionary for each object
        # Each object will be added on new line with it's attributes
        # Format for Rectange <id>,<width>,<height>,<x>,<y>
        # format for Square <id>,<size>,<x>,<y>
        # Each instance will be saved on a new line
        square_format: list[str] = ['id', 'size', 'x', 'y']
        rectangle_format: list[str] = [
                'id', 'width', 'height', 'x', 'y'
        ]
        text: str = ""
        for obj in list_objs:
            if hasattr(obj, 'size'):
                # Treat as Square
                values: list[int] = [
                        str(getattr(obj, attr)) for attr in square_format
                ]
                text = text + ",".join(values)
            else:
                # otherwise treat as Rectangle
                values: list[int] = [
                        str(getattr(obj, attr)) for attr in rectangle_format
                ]
                text = text + ",".join(values)
            # Add new line
            text += "\n"
        # Save to file
        # File name
        file_name: str = cls.__name__ + ".csv"
        with open(file_name, mode="w", encoding="utf-8") as file:
            # write to file
            file.write(text)

    @classmethod
    def load_from_file_csv(cls) -> list:
        """
        Class Method used to deserialize CSV

        Returns:
            - Python List Data Type <list>
        """
        # Formates
        square_format: list[str] = [
                "id", "size", "x", "y"
        ]
        rectangle_format: list[str] = [
                "id", "width", "height", "x", "y"
        ]

        # File name
        file_name: str = cls.__name__ + ".csv"
        # Read file
        content: str = ""
        with open(file_name, mode="r", encoding="utf-8") as file:
            # Read content
            content: str = file.read()
        # Check if content is empty or None
        if not content or content == "":
            return []

        # Deserialize
        content_list: list[str] = content.split("\n")

        # form the dictionary
        dictionaries: list[dict] = []
        for info in content_list:
            # Skip empty lines
            if not info:
                continue
            # Split data by sep = ","
            separat: list[int] = info.split(",")
            # Check the length of array to indicate if Square or Rectangle
            if len(separat) == 4:
                # assuming it is a square
                obj_dict: dict[str, int] = dict(
                        zip(square_format, map(int, separat))
                )
            else:
                # Assuming it is a rectangle
                obj_dict: dict[str, int] = dict(
                        zip(rectangle_format, map(int, separat))
                )
            dictionaries.append(obj_dict)
        # Return objects
        return [
                cls.create(**obj)
                for obj in dictionaries
        ]
