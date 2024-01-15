#!/usr/bin/python3


"""
File that contains class called Rectangle
"""


from .base import Base


class Rectangle(Base):
    """
    class that represents a two dimensional Rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Class instance initiation attributes.

        Args:
            - width: Width of the rectangle.
            - height: Height of the rectangle.
            - x: Postion according to the x-axis (default: 0)
            - y: Position according to the y-axis (default: 0)
        """
        # Initiate Super
        super().__init__(id)
        self.height = height
        self.width = width
        self.x = x
        self.y = y

    @staticmethod
    def validate_positive_integer(value: int, name: str) -> None:
        """
        Method used to validate value as positive integer

        Args:
            - value: integer input
            - name: variable name

        Returns:
            - Nothing, Just raises an error
        """
        # Validate integer type
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        # Check value of the input
        if value <= 0:
            raise ValueError(f"{name} must be > 0")

    @staticmethod
    def validate_integer(value: int, name: str) -> None:
        """
        Method used to validate if the value is an integer

        Args:
            - value: integer input
            - name: variable name

        Returns:
            Nothing, just Raises an Error
        """
        # Check type
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

    @staticmethod
    def validate_coordinate(value: int, name: str) -> None:
        """
        Static Method used to validate coordinates

        Args:
            - value: Integer value input
            - name: name of variable
        """
        # Check if it is equal or more than 0
        if value < 0:
            raise ValueError(f"{name} must be >= 0")

    @property
    def width(self) -> int:
        """
        Property method to get value to width

        Returns:
            - width of the rectangle as Python Integer Value <int>
        """
        return self.__width

    @width.setter
    def width(self, value: int) -> None:
        """
        Property Setter method for new value for width

        Args:
            - value: New value for width of rectangle

        Returns:
            - Nothing.
        """
        # Initiate variable name
        variable_name: str = "width"

        # Validate parameters
        self.validate_positive_integer(value, variable_name)

        # Set new value
        self.__width: int = value

    @property
    def height(self) -> int:
        """
        Property method to get value of height

        Returns:
            - height of the rectangle as Python Integer value <int>
        """
        return self.__height

    @height.setter
    def height(self, value) -> None:
        """
        Property Setter method used to set new value to height

        Args:
           - value: New value of height
        """
        # Initate variable name
        variable_name: str = 'height'

        # Validate value
        self.validate_positive_integer(value, variable_name)

        # Set new value to height
        self.__height: int = value

    @property
    def x(self) -> int:
        """
        Property method used to return X coordinate of rectangle

        Returns:
            - X-Coordinate of rectangle as python integer <int>
        """
        return self.__x

    @x.setter
    def x(self, value: int) -> None:
        """
        Property Setter method used to set new value to x-axis

        Args:
            - value: New x-coordinate for rectangle
        """
        # Initiate variable name
        variable_name: str = "x"
        # Validate value
        self.validate_integer(value, variable_name)
        self.validate_coordinate(value, variable_name)
        # Set New value
        self.__x: int = value

    @property
    def y(self) -> int:
        """
        Property Method used to return Y coordinate of rectangle

        Returns:
            - Y-Coordinate of rectangle as Python Integer <int>
        """
        return self.__y

    @y.setter
    def y(self, value: int) -> None:
        """
        Property Setter method used to set new value to y-axis

        Args:
            - value: New y-coordinate for rectangle
        """
        # Initiate variable name
        variable_name: str = 'y'
        # Validate value
        self.validate_integer(value, variable_name)
        self.validate_coordinate(value, variable_name)

        # Set New Value
        self.__y = value

    def area(self) -> int:
        """
        Method used to calculate Area of rectangle

        Returns:
            - Area of the rectangle
        """
        return self.height * self.width

    def display(self) -> None:
        """
        Represents Rectangle with Symbole
        """
        # Y - Axis Coordinates
        for new_line in range(self.y):
            print()

        for row in range(self.height):
            # X - Axis coordinates
            space_x: str = " " * self.x
            print(space_x, end="")
            for column in range(self.width):
                print("#", end='')
            print()

    def update(self, *args, **kwargs) -> None:
        """
        Method used to update class Rectangle
        """
        # Initiate instance attributes
        instance_attributes: list = [
                "id", "width", "height", "x", "y"
        ]
        # Skip **kwargs if *args exists
        if args:
            for attr in range(len(args)):
                # Instance key
                key: str = instance_attributes[attr]
                # Value from args
                value = args[attr]
                # Set the new value
                setattr(self, key, value)
        else:
            # Skipping **kwargs if *args exists
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self) -> dict[str, int]:
        """
        Method used to return a dictionary representation of class
        instance attributes

        Returns:
            - Dictionary that contains all class attributes
        """
        # Get attrs in dictionary
        class_attrs: dict[str, int] = {
                attr: getattr(self, attr) for attr in dir(self)
                if not attr.startswith("_")
                and not callable(getattr(self, attr))
        }
        # Return Dictionary
        return class_attrs

    def __str__(self) -> str:
        """
        Method used to return string representation
        """
        class_name: str = self.__class__.__name__
        x_y: str = f"{self.x}/{self.y}"
        width_height: str = f"{self.width}/{self.height}"
        return f"[{class_name}] ({self.id}) {x_y} - {width_height}"
