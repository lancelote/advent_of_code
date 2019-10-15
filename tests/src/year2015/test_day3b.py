"""Day 3 Puzzle Part 2 tests."""

import unittest

from src.year2015.day3b import solve


class TestSolve(unittest.TestCase):

    def test_returns_correct_result(self):
        self.assertEqual(solve('^v'), 3)
        self.assertEqual(solve('^>v<'), 3)
        self.assertEqual(solve('^v^v^v^v^v'), 11)
