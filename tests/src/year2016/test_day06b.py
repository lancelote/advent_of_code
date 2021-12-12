"""2016 - Day 6 Part 1: Signals and Noise tests."""
import unittest

from src.year2016.day06b import solve
from tests.src.year2016.test_day06a import EXAMPLE_TASK


class SolveTest(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(EXAMPLE_TASK), "advent")
