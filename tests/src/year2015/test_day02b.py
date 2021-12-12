"""Day 2 Puzzle Part 2 tests."""
import unittest

from src.year2015.day02b import solve


class TestSolve(unittest.TestCase):
    def test_returns_correct_result(self):
        self.assertEqual(solve("2x3x4"), 34)
        self.assertEqual(solve("1x1x10"), 14)
