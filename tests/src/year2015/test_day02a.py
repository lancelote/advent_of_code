"""2015 - Day 2 Part 1: I Was Told There Would Be No Math."""
import unittest

from src.year2015.day02a import process_data
from src.year2015.day02a import solve


class TestProcessData(unittest.TestCase):
    def test_returns_correct_result(self):
        self.assertEqual(process_data("1x2x3"), [(1, 2, 3)])
        self.assertEqual(process_data("1x2x3\n4x5x6"), [(1, 2, 3), (4, 5, 6)])


class TestSolve(unittest.TestCase):
    def test_returns_correct_result(self):
        self.assertEqual(solve("2x3x4"), 58)
        self.assertEqual(solve("1x1x10"), 43)
