#!/usr/bin/python3

"""Modules used in the Test"""
import unittest
import os
from io import StringIO
from unittest.mock import patch
from unittest import TestCase
from models.rectangle import Rectangle
from models.base import Base

class TestRectangleMethods(unittest.TestCase):
    """All tests for everything in the Rectangle class"""

    def default_nb_objects(self):
        """all instances are set to 0"""
        Base._Base__nb_objects = 0

    def test_new_rectangle(self):
        '''Creates a perfect rectangle'''
        rect = Rectangle(4, 3)
        #print(rect.id)

        self.assertEqual(rect.width, 4)
        self.assertEqual(rect.height, 3)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)
        #self.assertEqual(rect.id, 1)

    def test_rectangle_all_args(self):
        ''' all the args are provided '''

        rect = Rectangle(4, 3, 5, 3, 12)
        rect1 =Rectangle(5,6)
        #print(rect1.id)

        self.assertEqual(rect.width, 4)
        self.assertEqual(rect.height, 3)
        self.assertEqual(rect.x, 5)
        self.assertEqual(rect.y, 3)
        self.assertEqual(rect.id, 12)

    def test_new__rectangle_objs(self):
        '''Creates two different rect objs'''

        rect = Rectangle(5, 3)
        rect1 = Rectangle(5, 3)
        #print(rect.id)
        self.assertEqual(False, rect is rect1)
        self.assertEqual(False, rect.id == rect1.id)

    def test_if_rect_is_base(self):
        '''Test to see if the obj created is of Base'''

        rect = Rectangle(5, 3)
        #print(rect.id)
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
        with self.assertRaises(TypeError):
            rect = Rectangle('5', 4, 5, 3, 1)

    def test_check_for_integer_height(self):
        """testing the check for integer"""
        with self.assertRaises(TypeError):
            rect = Rectangle(5, '4', 5, 3, 1)

    def test_check_for_integer_x(self):
        """testing the check for integer"""
        with self.assertRaises(TypeError):
            rect = Rectangle(5, 4, '5', 3, 1)

    def test_check_for_integer_y(self):
        """testing the check for integer"""
        with self.assertRaises(TypeError):
            rect = Rectangle(5, 4, 5, '3', 1)

    def test_value_equal_zero_width(self):
        '''Test for value less or equal to zero'''

        with self.assertRaises(ValueError):
            rect = Rectangle(0, 1)

    def test_value_equal_zero_height(self):
        '''Test for value less or equal to zero'''

        with self.assertRaises(ValueError):
            rect = Rectangle(1, 0)

    def test_value_less_zero_width(self):
        '''Test for value less or equal to zero'''

        with self.assertRaises(ValueError):
            rect = Rectangle(-1, 1)

    def test_value_less_zero_height(self):
        '''Test for value less or equal to zero'''

        with self.assertRaises(ValueError):
            rect = Rectangle(4, -1)

    def test_value_less_zero_x(self):
        '''Test for value less or equal to zero'''

        with self.assertRaises(ValueError):
            rect = Rectangle(5, 3, -1, 2)

    def test_value_less_zero_y(self):
        '''Test for value less or equal to zero'''

        with self.assertRaises(ValueError):
            rect = Rectangle(5, 3, 5, -2)

    def test_area(self):
        '''Test for the area method '''

        rect = Rectangle(3, 2)
        self.assertEqual(rect.area(), 6)

    def test_area_new_values(self):
        '''Test for the area method with updated width and height'''

        rect = Rectangle(3, 2)
        self.assertEqual(rect.area(), 6)

        rect.width = 5
        self.assertEqual(rect.area(), 10)

        rect.height = 6
        self.assertEqual(rect.area(), 30)

    def test_area_more(self):
        rect = Rectangle(5, 9)
        self.assertEqual(rect.area(), 45)

        rect = Rectangle(10, 4)

        self.assertEqual(rect.area(), 40)


    def test_display(self):
        '''Test for '#' displayed'''

        r1 = Rectangle(2, 2)
        res = "##\n##\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_display_more(self):
        '''Test for '#' displayed'''

        r1 = Rectangle(2, 3)

        res = "##\n##\n##\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_display(self):
        '''Test for '#' displayed with a new value added'''

        r1 = Rectangle(2, 2)

        res = "##\n##\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

        r1.width = 3
        res = "###\n###\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)
