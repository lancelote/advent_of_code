"""Day 1 Puzzle Part 1 tests."""

import unittest

from src.year2015.day1a import solve


class TestSolve(unittest.TestCase):
    def test_returns_correct_result(self):
        self.assertEqual(solve("(())"), 0)
        self.assertEqual(solve("()()"), 0)
        self.assertEqual(solve("((("), 3)
        self.assertEqual(solve("(()(()("), 3)
        self.assertEqual(solve("))((((("), 3)
        self.assertEqual(solve("())"), -1)
        self.assertEqual(solve("))("), -1)
        self.assertEqual(solve(")))"), -3)
        self.assertEqual(solve(")())())"), -3)
