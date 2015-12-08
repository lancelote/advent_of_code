# coding=utf-8

"""
Day 1 Puzzle Part 2 tests
"""

import unittest

from src.day1b import solve


class TestSolve(unittest.TestCase):

    def test_solve(self):
        self.assertEqual(solve(')'), 1)
        self.assertEqual(solve('()())'), 5)
