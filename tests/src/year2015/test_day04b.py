"""2015 - Day 4 Part 2: The Ideal Stocking Stuffer."""
import unittest

from src.year2015.day04b import solve


class TestSolve(unittest.TestCase):
    def test_returns_correct_result(self):
        self.assertEqual(solve("yzbqklnj"), 9962624)
