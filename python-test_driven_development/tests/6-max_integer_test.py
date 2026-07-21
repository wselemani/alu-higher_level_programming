#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Defines test scenarios for the max_integer module function."""

    def test_ordered_list(self):
        """Tests an ordered list of values."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Tests an unordered list of values."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        """Tests an empty list argument."""
        self.assertIsNone(max_integer([]))

    def test_one_element_list(self):
        """Tests a single element array."""
        self.assertEqual(max_integer([7]), 7)

    def test_max_at_beginning(self):
        """Tests when the maximum value is located at index zero."""
        self.assertEqual(max_integer([9, 5, 3, 1]), 9)

    def test_negative_numbers(self):
        """Tests a collection composed entirely of negative integers."""
        self.assertEqual(max_integer([-1, -5, -3, -9]), -1)

    def test_mixed_numbers(self):
        """Tests a mix of positive and negative integers."""
        self.assertEqual(max_integer([-1, 5, 0, -9]), 5)


if __name__ == '__main__':
    unittest.main()
