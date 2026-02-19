#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function."""

    def test_max_at_end(self):
        """Test list where max integer is at the end."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        """Test list where max integer is at the beginning."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_in_middle(self):
        """Test list where max integer is in the middle."""
        self.assertEqual(max_integer([1, 4, 2, 3]), 4)

    def test_one_negative(self):
        """Test list with one negative number."""
        self.assertEqual(max_integer([1, -2, 3, 4]), 4)

    def test_only_negative(self):
        """Test list with only negative numbers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_single_element(self):
        """Test list with only one element."""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test an empty list."""
        self.assertEqual(max_integer([]), None)

    def test_no_args(self):
        """Test passing no arguments."""
        self.assertEqual(max_integer(), None)

    def test_floats(self):
        """Test list of floats."""
        self.assertEqual(max_integer([1.53, 6.33, -9.123, 15.2, 3.0]), 15.2)

    def test_ints_and_floats(self):
        """Test list of ints and floats."""
        self.assertEqual(max_integer([1.53, 15.5, -9, 15, 6]), 15.5)

    def test_string(self):
        """Test passing a string."""
        self.assertEqual(max_integer("School"), 'o')

    def test_list_of_strings(self):
        """Test list of strings."""
        self.assertEqual(max_integer(["Brennan", "Aaron", "Zack", "Bob"]), "Zack")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)


if __name__ == '__main__':
    unittest.main()
