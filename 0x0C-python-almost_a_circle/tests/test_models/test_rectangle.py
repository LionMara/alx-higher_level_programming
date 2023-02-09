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

    def setUp(self):
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

    def test_str(self):
        '''tests for the __str__ method'''

        rect = Rectangle(2, 5, 2, 4)
        res = "[Rectangle] (1) 2/4 - 2/5\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(rect)
            self.assertEqual(str_out.getvalue(), res)

    def test_str_2(self):
        '''tests for the __str__ method all values'''

        rect = Rectangle(4, 6, 2, 1, 12)
        res = "[Rectangle] (12) 2/1 - 4/6\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(rect)
            self.assertEqual(str_out.getvalue(), res)

        rect.id = 1
        rect.width = 7
        rect.height = 15
        res = "[Rectangle] (1) 2/1 - 7/15\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(rect)
            self.assertEqual(str_out.getvalue(), res)

    def test_str_three(self):
        '''str method with more changes '''

        rect = Rectangle(5, 10)
        res = "[Rectangle] (1) 0/0 - 5/10\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(rect)
            self.assertEqual(str_out.getvalue(), res)

        rect1 = Rectangle(34, 56, 12, 8)
        res1 = "[Rectangle] (2) 12/8 - 34/56\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(rect1)
            self.assertEqual(str_out.getvalue(), res1)

        rect2 = Rectangle(1, 1, 1, 1)
        res2 = "[Rectangle] (3) 1/1 - 1/1\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(rect2)
            self.assertEqual(str_out.getvalue(), res2)

    def test_str_four(self):
        '''more tests on the string method'''

        rct = Rectangle(3, 3)

        res = "[Rectangle] (1) 0/0 - 3/3"
        self.assertEqual(rct.__str__(), res)

    def test_display_axis(self):
        '''Rectangle modified to have x and y effect'''

        rect = Rectangle(5, 4, 1, 1)
        res = "\n #####\n #####\n #####\n #####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            rect.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_display_change_axis(self):
        '''valus of x and y are changed'''

        rect = Rectangle(3, 2)
        res = "###\n###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            rect.display()
            self.assertEqual(str_out.getvalue(), res)

        rect.x = 2
        res = "  ###\n  ###\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            rect.display()
            self.assertEqual(str_out.getvalue(), res)

        rect.y = 2
        res = "\n\n  ###\n  ###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            rect.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_dictionary(self):
        '''Testing the dictionary method'''

        rect = Rectangle(1, 2,3, 4, 1)
        res = "[Rectangle] (1) 3/4 - 1/2\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(rect)
            self.assertEqual(str_out.getvalue(), res)

        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)
        self.assertEqual(rect.id, 1)

        rect_dict = rect.to_dictionary()

        result = "<class 'dict'>\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(type(rect_dict))
            self.assertEqual(str_out.getvalue(), result)

    def test_dictionary_more(self):
        '''Testing the dictionary method'''

        rect = Rectangle(2, 2, 2, 2)
        res = "[Rectangle] (1) 2/2 - 2/2\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(rect)
            self.assertEqual(str_out.getvalue(), res)

        rect1 = Rectangle(5, 7)
        res1 = "[Rectangle] (2) 0/0 - 5/7\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(rect1)
            self.assertEqual(str_out.getvalue(), res1)

        rect_dict = rect.to_dictionary()
        rect1.update(**rect_dict)

        self.assertEqual(rect.width, rect1.width)
        self.assertEqual(rect.height, rect1.height)
        self.assertEqual(rect.x, rect1.x)
        self.assertEqual(rect.y, rect1.y)
        self.assertEqual(rect.id, rect1.id)

        result = "<class 'dict'>\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(type(rect_dict))
            self.assertEqual(str_out.getvalue(), result)
