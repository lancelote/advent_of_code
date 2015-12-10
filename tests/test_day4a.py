# coding=utf-8
# pylint: disable=missing-docstring

"""
Day 4 Puzzle Part 1 tests
"""

import unittest

from src.day4a import solve


class TestSolve(unittest.TestCase):

    def test_returns_result(self):
        self.assertEqual(solve('abcdef'), 609043)
        self.assertEqual(solve('pqrstuv'), 1048970)
        self.assertEqual(solve('yzbqklnj'), 282749)
