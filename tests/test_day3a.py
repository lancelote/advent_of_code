# coding=utf-8
# pylint: disable=missing-docstring

"""
Day 3 Puzzle Part 1 tests
"""

import unittest

from src.day3a import solve


class TestSolve(unittest.TestCase):

    def test_returns_result(self):
        self.assertEqual(solve('>'), 2)
        self.assertEqual(solve('^>v<'), 4)
        self.assertEqual(solve('^v^v^v^v^v'), 2)
