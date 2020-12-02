"""Day 6 Puzzle Part 1 tests."""
import unittest

from src.year2015.day6a import process_data
from src.year2015.day6a import solve
from src.year2015.day6a import update_light


class TestProcessData(unittest.TestCase):
    def test_returns_correct_result(self):
        turn_on = process_data("turn on 489,959 through 759,964")
        turn_off = process_data("turn off 820,516 through 871,914")
        toggle = process_data("toggle 120,314 through 745,489")

        self.assertEqual(turn_on, [("turn on", (489, 959), (759, 964))])
        self.assertEqual(turn_off, [("turn off", (820, 516), (871, 914))])
        self.assertEqual(toggle, [("toggle", (120, 314), (745, 489))])


class TestUpdateLight(unittest.TestCase):
    def test_returns_correct_result(self):
        self.assertFalse(update_light("toggle", True))
        self.assertTrue(update_light("toggle", False))
        self.assertTrue(update_light("turn on", True))
        self.assertTrue(update_light("turn on", False))
        self.assertFalse(update_light("turn off", False))
        self.assertFalse(update_light("turn off", True))


class TestSolve(unittest.TestCase):
    def test_returns_correct_result(self):
        self.assertEqual(solve("turn on 0,0 through 999,999"), 10 ** 6)
        self.assertEqual(solve("toggle 0,0 through 999,0"), 1000)
