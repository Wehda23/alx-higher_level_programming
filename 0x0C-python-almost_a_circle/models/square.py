#!/usr/bin/python3
"""
File that contains class called Square
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A class that represents 2D Square
    """
    def __init__(self, size: int, x: int = 0, y: int = 0, id=None):
        """
        Instance initiation method

        Args:
            - size: Size of the rectangle dimensions
            - x: X-Axis coordinate
            - y: Y-Axis Coordinate
            - id: id of the instance
        """
        super().__init__(size, size, x, y, id)

    # overloading parent method.
    def __str__(self) -> str:
        """
        Method used to return representation of instance
        """
        class_name: str = self.__class__.__name__
        x_y: str = f"{self.x}/{self.y}"
        return f"[{class_name}] ({self.id}) {x_y} - {self.width}"
    
    @property
    def size(self) -> int:
        """
        Property method used to retrieve the size
        of the Square

        Returns:
            - Size of the Square
        """
        return self.width

    @size.setter
    def size(self, value) -> None:
        """
        Property Setter method used to renew value of size

        Args:
            - value: Is the new size value
        """
        # First do it with width then height
        self.height = value
        self.width = value