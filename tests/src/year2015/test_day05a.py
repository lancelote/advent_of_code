"""Day 5 Puzzle Part 1 tests."""
import unittest

from src.year2015.day05a import is_nice
from src.year2015.day05a import process_data


class TestIsNice(unittest.TestCase):
    def test_returns_correct_result(self):
        self.assertTrue(is_nice("ugknbfddgicrmopn"))
        self.assertTrue(is_nice("aaa"))
        self.assertFalse(is_nice("jchzalrnumimnmhp"))
        self.assertFalse(is_nice("haegwjzuvuyypxyu"))
        self.assertFalse(is_nice("dvszwmarrgswjxmb"))


class TestProcessData(unittest.TestCase):
    def test_returns_correct_result(self):
        self.assertEqual(process_data("ab\ncd\n"), ["ab", "cd"])
        self.assertEqual(process_data("ab"), ["ab"])
