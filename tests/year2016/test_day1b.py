# pylint: disable=missing-docstring, invalid-name

"""
2016 - Day 1 Puzzle Part 2 tests
"""

import unittest


from src.year2016.day1b import solve


class SolveTest(unittest.TestCase):

    def test_sample_path(self):
        self.assertEqual(solve('R8, R4, R4, R8'), 4)
