"""Day 5 Puzzle Part 2 tests."""

import unittest

from src.year2015.day5b import is_nice


class TestIsNice(unittest.TestCase):
    def test_returns_correct_result(self):
        self.assertTrue(is_nice("qjhvhtzxzqqjkmpb"))
        self.assertTrue(is_nice("xxyxx"))
        self.assertFalse(is_nice("uurcxstgmygtbstg"))
        self.assertFalse(is_nice("ieodomkazucvgmuy"))
        self.assertFalse(is_nice("aaa"))
