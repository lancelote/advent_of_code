# coding=utf-8
# pylint: disable=missing-docstring

"""
Day 2 Puzzle Part 1 tests
"""

import unittest

from src.day2a import process_data, solve


class TestProcessData(unittest.TestCase):

    def test_returns_correct_result(self):
        self.assertEqual(process_data('1x2x3'), [(1, 2, 3)])
        self.assertEqual(process_data('1x2x3\n4x5x6'), [(1, 2, 3), (4, 5, 6)])


class TestSolve(unittest.TestCase):

    def test_returns_correct_result(self):
        self.assertEqual(solve('2x3x4'), 58)
        self.assertEqual(solve('1x1x10'), 43)
