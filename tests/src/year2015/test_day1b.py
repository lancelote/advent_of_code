"""Day 1 Puzzle Part 2 tests."""
import unittest

from src.year2015.day1b import solve


class TestSolve(unittest.TestCase):
    def test_returns_correct_result(self):
        self.assertEqual(solve(")"), 1)
        self.assertEqual(solve("()())"), 5)
