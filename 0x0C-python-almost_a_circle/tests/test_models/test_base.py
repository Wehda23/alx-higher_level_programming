import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0  # Reset the counter for each test case

    def test_create_method(self):
        # Test create method for Rectangle
        rect_dict = {"id": 1, "width": 4, "height": 5, "x": 1, "y": 2}
        rect_instance = Rectangle.create(**rect_dict)
        self.assertIsInstance(rect_instance, Rectangle)
        self.assertEqual(str(rect_instance), "[Rectangle] (1) 1/2 - 4/5")

        # Test create method for Square
        square_dict = {"id": 2, "size": 3, "x": 0, "y": 0}
        square_instance = Square.create(**square_dict)
        self.assertIsInstance(square_instance, Square)
        self.assertEqual(str(square_instance), "[Square] (2) 0/0 - 3")

if __name__ == '__main__':
    unittest.main()

