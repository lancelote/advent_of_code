"""2015 - Day 3 Part 1: Perfectly Spherical Houses in a Vacuum."""
import unittest

from src.year2015.day03a import solve


class TestSolve(unittest.TestCase):
    def test_returns_correct_result(self):
        self.assertEqual(solve(">"), 2)
        self.assertEqual(solve("^>v<"), 4)
        self.assertEqual(solve("^v^v^v^v^v"), 2)
