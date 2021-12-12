"""Day 4 Puzzle Part 1 tests."""
import unittest

from src.year2015.day04a import solve


class TestSolve(unittest.TestCase):
    def test_returns_correct_result(self):
        self.assertEqual(solve("abcdef"), 609043)
        self.assertEqual(solve("pqrstuv"), 1048970)
        self.assertEqual(solve("yzbqklnj"), 282749)
