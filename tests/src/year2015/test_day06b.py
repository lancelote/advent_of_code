"""2015 - Day 6 Part 2: Probably a Fire Hazard."""

import unittest

from src.year2015.day06a import Command
from src.year2015.day06b import solve
from src.year2015.day06b import update_light


class TestSolve(unittest.TestCase):
    def test_returns_correct_result(self):
        self.assertEqual(solve("turn on 0,0 through 0,0"), 1)
        self.assertEqual(solve("toggle 0,0 through 999,999"), 2 * 10**6)

    def test_light_brightness_can_not_be_negative(self):
        self.assertEqual(solve("turn off 0,0 through 0,0"), 0)


class TestUpdateLight(unittest.TestCase):
    def test_returns_correct_result(self):
        self.assertEqual(update_light(Command.TOGGLE, 0), 2)
        self.assertEqual(update_light(Command.TURN_ON, 0), 1)
        self.assertEqual(update_light(Command.TURN_OFF, 1), 0)

    def test_brightness_can_not_be_negative(self):
        self.assertEqual(update_light(Command.TURN_OFF, 0), 0)
