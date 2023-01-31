#!/usr/bin/python3
'''unittest module'''
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    '''Testcases used for 6-max-intger'''

    def test_ordered_list(self):
        '''Test ordered list of ints'''
        ordered_list = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered_list), 4)

    def test_unordered_list(self):
        '''Test unordered list of ints'''
        unordered_list = [3, 2, 4, 1]
        self.assertEqual(max_integer(unordered_list), 4)

    def test_max_at_start_of_listt(self):
        '''Test for max value at start'''
        list_unordered = [4, 1, 3, 2]
        self.assertEqual(max_integer(list_unordered), 4)

    def test_empty_list(self):
        '''Empty list'''
        list_empty = []
        self.assertEqual(max_integer(list_empty), None)

    def test_one_element(self):
        '''a list of one element'''
        list_one_ele = [1]
        self.assertEqual(max_integer(list_one_ele), 1)

    def test_float_list(self):
        ''' a list of floats '''
        list_floats = [1.0, 2.3, 3.4, 5.6, 7.8]
        self.assertEqual(max_integer(list_floats), 7.8)

    def test_float_ints(self):
        '''list of both floats and ints'''
        list_float_ints = [1, 4.5, 3, 2.5, 8]
        self.assertEqual(max_integer(list_float_ints), 8)

    def test_string(self):
        '''test for a string'''
        string = 'Brennan'
        self.assertEqual(max_integer(string), 'r')

    def test_list_of_strings(self):
        ''' list of strngs'''
        list_string = ['Brennan', 'is', 'my', 'name']
        self.assertEqual(max_integer(list_string), 'name')

    def test_empty_string(self):
        '''test for empty string'''
        empty_string = ''
        self.assertEqual(max_integer(empty_string), None)


if __name__ == '__main__':
    unittest.main()
