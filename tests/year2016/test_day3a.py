"""2016 - Day 3 Puzzle Part 1 tests."""

import unittest
from itertools import permutations

from src.year2016.day3a import process_data, is_bad, solve


class ProcessDataTest(unittest.TestCase):

    def test_process_single_line(self):
        line = '    4   21  894'
        expected_triangles = [(4, 21, 894)]
        self.assertEqual(process_data(line), expected_triangles)

    def test_process_multiple_lines(self):
        lines = '  419  794  987\n  424  797  125'
        expected_triangles = [(419, 794, 987), (424, 797, 125)]
        self.assertEqual(process_data(lines), expected_triangles)


class IsBadTest(unittest.TestCase):

    def test_bad(self):
        for bad_triangle in permutations((5, 10, 25)):
            self.assertTrue(is_bad(bad_triangle))

    def test_two_side_equal(self):
        self.assertFalse(is_bad((1, 10, 10)))

    def test_all_sides_equal(self):
        self.assertFalse(is_bad((5, 5, 5)))

    def test_sum_of_shortest_equal_to_longest(self):
        self.assertTrue(is_bad((4, 6, 10)))


class SolveTest(unittest.TestCase):

    def test_solve(self):
        data = '    1 2 3\n    4 5 6\n   17 8 100'
        self.assertEqual(solve(data), 1)
