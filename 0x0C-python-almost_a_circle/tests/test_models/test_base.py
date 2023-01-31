#!/usr/bin/python3

import unittest
from models.base import Base
from io import StringIO
from unittest import TestCase
from unittest.mock import patch


class TestBaseMethods(unittest.TestCase):
    def test_automatic_base(self):
        '''Anytime base is called'''

        Base._Base__nb_objects = 0
    def test_id_provided(self):
        '''Test for id provided'''
        b1 = Base(12)
        self.assertEqual(b1.id, 12)

    def test_id_not_given(self):
        '''Test when id is not provided'''
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id -1)


    def test_no_arg_three(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_arg_is_none(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, 1)

    def test_arg_unique(self):
        b1 = Base(12)
        self.assertEqual(b1.id, 12)

    def test_nb_instances_after_id(self):
        base1 = Base()
        base2 = Base(12)
        base3 = Base()
        self.assertEqual(base1.id, base3.id - 1)

    def test_nb_instances_private(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

    def test_arg_is_str(self):
        self.assertEqual("clone", Base("clone").id)

    def test_float(self):
        self.assertEqual(5.5, Base(5.5).id)

    def test_id_complex(self):
        self.assertEqual(complex(8), Base(complex(8)).id)

    def test_id_is_dict(self):
        self.assertEqual({'a':'A', 'b':'B'}, Base({'a':'A', 'b':'B'}).id)


    def test_id_is_boolean(self):
        self.assertEqual(True, Base(True).id)

    def test_id_is_list(self):
        self.assertEqual([1,2,3], Base([1,2,3]).id)


    def test_id_is_tuple(self):
        self.assertEqual((1,2), Base((1,2)).id)

    def test_id_is_set(self):
        self.assertEqual({1,2,3,4}, Base({1,2,3,4}).id)

    def test_frozen_set(self):
        self.assertEqual(frozenset({1, 2, 3}), Base(frozenset({1,2,3})).id)

    def test_id_is_range(self):
        self.assertEqual(range(4), Base(range(4)).id)

    def test_id_is_bytes(self):
        self.assertEqual(b'clinton', Base(b'clinton').id)
