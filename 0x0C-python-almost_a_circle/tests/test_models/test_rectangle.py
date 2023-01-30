#!/usr/bin/python3
"""Modules used in the Test"""
import unittest
from unittest import TestCase
from models.rectangle import Rectangle
from models.base import Base

class TestRectangleMethods(unittest.TestCase):
    """All tests for everything in the Rectangle class"""
    def test_new_rectangle(self):
        '''Creates a perfect rectangle'''
        rect = Rectangle(4, 3)

        self.assertEqual(rect.width, 4)
        self.assertEqual(rect.height, 3)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.id, 1)

    def test_rectangle_all_args(self):
        ''' all the args are provided '''

        rect = Rectangle(4, 3, 5, 3, 12)

        self.assertEqual(rect.width, 4)
        self.assertEqual(rect.height, 3)
        self.assertEqual(rect.x, 5)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.id, 12)

    def test_new__rectangle_objs(self):
        '''Creates two different rect objs'''

        rect = Rectangle(5, 3)
        rect1 = Rectangle(5, 3)
        self.assertEqual(False, rect is rect1)
        self.assertEqual(Flase, rect.id == rect1.id)

    def test_if_rect_is_base(self):
        '''Test to see if the obj created is of Base'''

        rect = Rectangle(5, 3)
        self.assertEqual(True, isinstance(rect, Base))

    def test_no_args(self):
        '''pass no args '''

        with self.assertRaises(TypeError):
            rect = Rectangle()

    def test_private_width(self):
        '''Access private attributes'''

        rect = Rectangle(5, 3)

        with self.assertRaises(AttributeError):
            rect.__width

    def test_private_height(self):
        '''Access private attributes'''

        rect = Rectangle(5, 3)

        with self.assertRaises(AttributeError):
            rect.__height

    def test_private_x(self):
        '''Access private attributes'''

        rect = Rectangle(5, 3)

        with self.assertRaises(AttributeError):
            rect.__x

    def test_private_y(self):
        '''Access private attributes'''

        rect = Rectangle(5, 3)

        with self.assertRaises(AttributeError):
            rect.__y

    def test_check_for_integer_width(self):
        """testing the check for integer"""
        with assertRaises(TypeError):
            rect = Rectangle('5', 4, 5, 3, 1)

    def test_check_for_integer_height(self):
        """testing the check for integer"""
        with assertRaises(TypeError):
            rect = Rectangle(5, '4', 5, 3, 1)

    def test_check_for_integer_x(self):
        """testing the check for integer"""
        with assertRaises(TypeError):
            rect = Rectangle(5, 4, '5', 3, 1)

    def test_check_for_integer_y(self):
        """testing the check for integer"""
        with assertRaises(TypeError):
            rect = Rectangle(5, 4, 5, '3', 1)

    def test_value_equal_zero_width(self):
        '''Test for value less or equal to zero'''

        with assertRaises(ValueError):
            rect = Rectangle(0, 1)

    def test_value_equal_zero_height(self):
        '''Test for value less or equal to zero'''

        with assertRaises(ValueError):
            rect = Rectangle(1, 0)

    def test_value_less_zero_width(self):
        '''Test for value less or equal to zero'''

        with assertRaises(ValueError):
            rect = Rectangle(-1, 1)

    def test_value_less_zero_height(self):
        '''Test for value less or equal to zero'''

        with assertRaises(ValueError):
            rect = Rectangle(4, -1)

    def test_value_less_zero_x(self):
        '''Test for value less or equal to zero'''

        with assertRaises(ValueError):
            rect = Rectangle(5, 3, -1, 2)

    def test_value_less_zero_y(self):
        '''Test for value less or equal to zero'''

        with assertRaises(ValueError):
            rect = Rectangle(5, 3, 5, -2)
