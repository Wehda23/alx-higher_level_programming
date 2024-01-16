#!/usr/bin/python3
"""
Unittesting for square.py
"""

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    Class used to unittest Square Class
    """

    def setUp(self):
        """
        Setting up for tests
        """
        self.square1 = Square(5, 2, 3, 1)
        self.square2 = Square(8, 1, 2, 10)

    def test_str_representation(self):
        """
        Testing Str
        """
        self.assertEqual(str(self.square1), "[Square] (1) 2/3 - 5")
        self.assertEqual(str(self.square2), "[Square] (10) 1/2 - 8")

    def test_size_property(self):
        """
        Testing size property
        """
        self.assertEqual(self.square1.size, 5)
        self.assertEqual(self.square2.size, 8)

    def test_size_setter(self):
        """
        Testing setter
        """
        self.square1.size = 10
        self.assertEqual(self.square1.size, 10)
        self.assertEqual(self.square1.width, 10)
        self.assertEqual(self.square1.height, 10)

    def test_update_method(self):
        """
        Testing Update method
        """
        self.square1.update(4, 6, 1, 4)
        self.assertEqual(str(self.square1), "[Square] (4) 1/4 - 6")
        self.square2.update(size=12, y=5)
        self.assertEqual(str(self.square2), "[Square] (10) 1/5 - 12")

    def test_to_dictionary_method(self):
        """
        Testing to_dictionary method
        """
        dict1 = {"id": 1, "size": 5, "x": 2, "y": 3}
        dict2 = {"id": 10, "size": 8, "x": 1, "y": 2}
        self.assertEqual(self.square1.to_dictionary(), dict1)
        self.assertEqual(self.square2.to_dictionary(), dict2)

                                 
if __name__ == '__main__':
    unittest.main()
