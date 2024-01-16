#!/usr/bin/python3
"""
Defines unittests for rectangle.py
"""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Class used to unittest rectangle
    """

    def setUp(self):
        """
        Setting up for unittesting
        """
        self.rect1 = Rectangle(4, 5, 1, 2, 1)
        self.rect2 = Rectangle(7, 8, 3, 4, 10)

    def test_str_representation(self):
        """
        Testing str
        """
        self.assertEqual(str(self.rect1), "[Rectangle] (1) 1/2 - 4/5")
        self.assertEqual(str(self.rect2), "[Rectangle] (10) 3/4 - 7/8")

    def test_area_method(self):
        """
        Testing Area method
        """
        self.assertEqual(self.rect1.area(), 20)
        self.assertEqual(self.rect2.area(), 56)

    def test_update_method(self):
        """
        Testing Update method
        """
        self.rect1.update(4, 6, 1, 0, 2)
        self.assertEqual(str(self.rect1), "[Rectangle] (4) 0/2 - 6/1")

        self.rect2.update(height=12, y=5)
        self.assertEqual(str(self.rect2), "[Rectangle] (10) 3/5 - 7/12")

    def test_to_dictionary_method(self):
        """
        Testing to_dictionary method
        """
        dict1 = {"id": 1, "width": 4, "height": 5, "x": 1, "y": 2}
        dict2 = {"id": 10, "width": 7, "height": 8, "x": 3, "y": 4}

        self.assertEqual(self.rect1.to_dictionary(), dict1)
        self.assertEqual(self.rect2.to_dictionary(), dict2)


if __name__ == '__main__':
    unittest.main()
