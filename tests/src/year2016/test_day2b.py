"""2016 - Day 2 Puzzle Part 2 tests."""
import unittest

from src.year2016.day2b import solve


class SampleSolve(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve("ULL\nRRDDD\nLURDL\nUUUUD"), "5DB3")
