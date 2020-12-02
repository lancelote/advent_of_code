"""2016 - Day 1 Puzzle Part 2 tests."""
import unittest

from src.year2016.day1b import in_between
from src.year2016.day1b import Point
from src.year2016.day1b import solve


class InBetweenTest(unittest.TestCase):
    def test_east(self):
        points = list(in_between(Point(), Point(2, 0)))
        self.assertEqual(points, [Point(1, 0), Point(2, 0)])

    def test_west(self):
        points = list(in_between(Point(), Point(-2, 0)))
        self.assertEqual(points, [Point(-1, 0), Point(-2, 0)])

    def test_north(self):
        points = list(in_between(Point(), Point(0, 2)))
        self.assertEqual(points, [Point(0, 1), Point(0, 2)])

    def test_south(self):
        points = list(in_between(Point(), Point(0, -2)))
        self.assertEqual(points, [Point(0, -1), Point(0, -2)])

    def test_long_run(self):
        points = list(in_between(Point(), Point(0, 3)))
        self.assertListEqual(points, [Point(0, 1), Point(0, 2), Point(0, 3)])

    def test_same_points(self):
        with self.assertRaises(ValueError):
            list(in_between(Point(), Point()))

    def test_not_horizontal_or_vertical(self):
        with self.assertRaises(ValueError):
            list(in_between(Point(0, 0), Point(1, 1)))


class SolveTest(unittest.TestCase):
    def test_sample_path(self):
        self.assertEqual(solve("R8, R4, R4, R8"), 4)

    def test_no_points_are_visited(self):
        with self.assertRaises(ValueError):
            solve("R4 R4 R4")
