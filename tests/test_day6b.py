# coding=utf-8
# pylint: disable=missing-docstring,invalid-name

"""
Day 6 Puzzle Part 2 tests
"""

import unittest

from src.day6b import solve, update_light


class TestSolve(unittest.TestCase):

    def test_returns_correct_result(self):
        self.assertEqual(solve('turn on 0,0 through 0,0'), 1)
        self.assertEqual(solve('toggle 0,0 through 999,999'), 2*10**6)

    def test_light_brightness_can_not_be_negative(self):
        self.assertEqual(solve('turn off 0,0 through 0,0'), 0)


class TestUpdateLight(unittest.TestCase):

    def test_returns_correct_result(self):
        self.assertEqual(update_light('toggle', 0), 2)
        self.assertEqual(update_light('turn on', 0), 1)
        self.assertEqual(update_light('turn off', 1), 0)

    def test_brightness_can_not_be_negative(self):
        self.assertEqual(update_light('turn off', 0), 0)
