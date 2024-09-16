"""2015 - Day 3 Part 2: Perfectly Spherical Houses in a Vacuum."""

import unittest

from src.year2015.day03b import solve


class TestSolve(unittest.TestCase):
    def test_returns_correct_result(self):
        self.assertEqual(solve("^v"), 3)
        self.assertEqual(solve("^>v<"), 3)
        self.assertEqual(solve("^v^v^v^v^v"), 11)
