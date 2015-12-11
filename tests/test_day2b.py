# coding=utf-8
# pylint: disable=missing-docstring

"""
Day 2 Puzzle Part 2 tests
"""

import unittest

from src.day2b import solve


class TestSolve(unittest.TestCase):

    def test_returns_correct_result(self):
        self.assertEqual(solve('2x3x4'), 34)
        self.assertEqual(solve('1x1x10'), 14)
