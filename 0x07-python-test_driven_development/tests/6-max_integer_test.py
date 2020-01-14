#!/usr/bin/python3


"""
Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_normal_list(self):
        lista = [1, 2, 3, 4]
        self.assertEqual(max_integer(lista), 4)
        self.assertEqual(max_integer([[1230], [2321], [6534], [5432]]), [6534])

    def test_with_string(self):
        with self.assertRaises(TypeError):
            lista = [1, "paula", 3, 4]
            max_integer(lista)
        with self.assertRaises(TypeError):
            max_integer(4, 5)
        with self.assertRaises(TypeError):
            max_integer(["Yup", 11, 4, -21.5, 7])

    def test_with_negative(self):
        lista = [1, 2, 3, -4]
        self.assertEqual(max_integer(lista), 3)
        self.assertEqual(max_integer([-1, -2, -5, -7]), -1)
        self.assertEqual(max_integer([7, -7, -7, 7]), 7)

    def empty_list(self):
        lista = []
        self.assertIsNone(max_integer(lista))

    def test_OneElement(self):
        self.assertEqual(max_integer([33]), 33)
