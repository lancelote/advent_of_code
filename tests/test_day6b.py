# coding=utf-8
# pylint: disable=missing-docstring,invalid-name

"""
Day 6 Puzzle Part 2 tests
"""

import unittest

from src.day6b import solve


class TestSolve(unittest.TestCase):

    def test_returns_correct_result(self):
        self.assertEqual(solve('turn on 0,0 through 0,0'), 1)
        self.assertEqual(solve('toggle 0,0 through 999,999'), 2*10**6)

    def test_light_brightness_can_not_be_negative(self):
        self.assertEqual(solve('turn of 0,0 through 0,0'), 0)
