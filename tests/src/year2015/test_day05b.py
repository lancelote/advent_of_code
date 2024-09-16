"""2015 - Day 5 Part 1: Doesn't He Have Intern-Elves For This."""

import unittest

from src.year2015.day05b import is_nice


class TestIsNice(unittest.TestCase):
    def test_returns_correct_result(self):
        self.assertTrue(is_nice("qjhvhtzxzqqjkmpb"))
        self.assertTrue(is_nice("xxyxx"))
        self.assertFalse(is_nice("uurcxstgmygtbstg"))
        self.assertFalse(is_nice("ieodomkazucvgmuy"))
        self.assertFalse(is_nice("aaa"))
