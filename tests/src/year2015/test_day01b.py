"""2015 - Day 1 Part 2: Not Quite Lisp."""
import unittest

from src.year2015.day01b import solve


class TestSolve(unittest.TestCase):
    def test_returns_correct_result(self):
        self.assertEqual(solve(")"), 1)
        self.assertEqual(solve("()())"), 5)
