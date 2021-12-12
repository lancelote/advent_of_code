"""Day 4 Puzzle Part 2 tests."""
import unittest

from src.year2015.day04b import solve


class TestSolve(unittest.TestCase):
    def test_returns_correct_result(self):
        self.assertEqual(solve("yzbqklnj"), 9962624)
