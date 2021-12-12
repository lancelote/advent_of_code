"""2016 - Day 3 Puzzle Part 2 tests."""
import unittest

from src.year2016.day03b import process_data
from src.year2016.day03b import solve


class ProcessDataTest(unittest.TestCase):
    def test_process_data(self):
        task = "1 5 9\n2 6 10\n3 7 11\n4 8 12"
        expected_triangles = [
            (1, 2, 3),
            (4, 5, 6),
            (7, 8, 9),
            (10, 11, 12),
        ]
        self.assertEqual(process_data(task), expected_triangles)


class SolveTest(unittest.TestCase):
    def test_solve(self):
        task = "1 4 2\n2 5 3\n  3 6 7\n"
        self.assertEqual(solve(task), 1)
