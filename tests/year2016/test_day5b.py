"""2016 - Day 5 Part 2: How About a Nice Game of Chess tests."""

import unittest
from unittest import mock  # type: ignore

from src.year2016.day5b import solve


class SolveTest(unittest.TestCase):

    def test_solve(self):
        with mock.patch('src.year2016.day5b.print_password'):
            self.assertEqual(solve('abc'), '05ace8e3')
