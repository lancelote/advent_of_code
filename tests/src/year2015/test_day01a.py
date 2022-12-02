"""2015 - Day 1 Part 1: Not Quite Lisp."""
import unittest

from src.year2015.day01a import solve


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
