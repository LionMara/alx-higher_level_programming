#!/usr/bin/python3
'''Modules imported for Square testing'''
import unittest
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base

class TestSquareMethods(unittest.TestCase):
    '''these are test cases used for the Square class'''

    def setUp(self):
        ''' invoked for each test'''

        Base._Base__nb_objects = 0

    def test_square(self):
        '''create a new square with just size'''

        new_square = Square(3)
        self.assertEqual(new_square.size, 3)
        self.assertEqual(new_square.width, 3)
        self.assertEqual(new_square.height, 3)
        self.assertEqual(new_square.x, 0)
        self.assertEqual(new_square.y, 0)
        self.assertEqual(new_square.id, 1)

    def test_square_all_values(self):
        ''' all values are provided'''

        new_square = Square(2, 5, 5, 4)

        self.assertEqual(new_square.size, 2)
        self.assertEqual(new_square.width, 2)
        self.assertEqual(new_square.height, 2)
        self.assertEqual(new_square.x, 5)
        self.assertEqual(new_square.y, 5)
        self.assertEqual(new_square.id, 4)

    def test_many_squares(self):
        '''checks squares with same attributes'''

        new_square = Square(1, 1)
        newer_square = Square(1, 1)

        self.assertEqual(False, new_square is newer_square)
        self.assertEqual(False, new_square.id is newer_square.id)

    def test_Square_is_Base(self):
        '''checks if Square is an instance of Base'''

        new_square = Square(2)
        self.assertEqual(True, isinstance(new_square, Base))

    def test_Square_is_Rectangle(self):
        '''checks if Square is an instance of Rectangle'''

        new_square = Square(2)
        self.assertEqual(True, isinstance(new_square, Rectangle))


"""
    def test_no_args(self):
        '''Testing for no args provided'''

        with self.assertRaises(TypeError):
            new_square = Square()
    def test_extra_args(self):
        '''Testing with extra args provided'''

        with self.assertRaises(TypeError):
            new_square = Square(1, 1, 1, 1, 1)

    def test_private_attribute_width(self):
        '''Testing with private attribute provided'''

        new_square = Square(4)
        with self.assertRaises(TypeError):
            new_square.__width

    def test_private_attribute_height(self):
        '''Testing with private attribute provided'''

        new_square = Square(4)
        with self.assertRaises(TypeError):
            new_square.__height

    def test_private_attribute_x(self):
        '''Testing with private attribute provided'''

        new_square = Square(4)
        with self.assertRaises(TypeError):
            new_square.__x

    def test_private_attribute_y(self):
        '''Testing with private attribute provided'''

        new_square = Square(4)
        with self.assertRaises(TypeError):
            new_square.__y

    def test_wrong_type_siz(self):
        '''test for wrong type'''

        with self.assertRaises(TypeError):
            new_square = ('2', 2, 2, 2)
    def test_wrong_type_x(self):
        '''test for wrong type'''

        with self.assertRaises(TypeError):
            new_square = (2, '2', 2, 2)

    def test_wrong_type_y(self):
        '''test for wrong type'''

        with self.assertRaises(TypeError):
            new_square = (2, 2, '2', 2)

    def test_wrong_type_id(self):
        '''test for wrong type'''

        with self.assertRaises(TypeError):
            new_square = (2, 2, 2, '2')

    def test_invalid_value_zero(self):
        '''test for invalid values'''

        with self.assertRaises(ValueError):
            new_square = (0)

    def test_invalid_value_negative(self):
        '''test for invalid values'''

        with self.assertRaises(ValueError):
            new_square = (1, -1)

    def test_area(self):
        ''' test for area'''

        new_square = Square(5)
        self.assertEqual(new_square.area(), 25)
"""
