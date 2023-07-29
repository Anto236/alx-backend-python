#!/usr/bin/env python3
"""
Unit tests for utils.access_nested_map
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    TestAccessNestedMap class to test the utils.access_nested_map function
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_output):
        """
        Test the utils.access_nested_map function with different inputs.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_output)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Test that a KeyError is raised for specific inputs.
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)
