#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInt(unittest.TestCase):
    def test_max_int(self):
        self.assertIsNone(max_integer([]))

        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 1, 2, 3]), 4)
        self.assertEqual(max_integer([1, 2, 4, 3]), 4)

        self.assertEqual(max_integer([1, 2, -3, 4]), 4)
        self.assertEqual(max_integer([-4, 1, 2, 3]), 3)
        self.assertEqual(max_integer([-12, -7, 0]), 0)

        # self.assertRaises(TypeError, max_integer, 12)
