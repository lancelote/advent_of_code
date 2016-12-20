# pylint: disable=missing-docstring, invalid-name

"""2016 - Day 1 Puzzle Part 2 tests."""

import unittest


from src.year2016.day1b import solve, in_between, Point


class InBetweenTest(unittest.TestCase):

    def test_east(self):
        pass

    def test_west(self):
        pass

    def test_north(self):
        pass

    def test_south(self):
        pass

    def test_long_run(self):
        result = list(in_between(Point(), Point(0, 3)))
        # ToDo: Comparison of object list is failed without a good reason
        self.assertListEqual(result, [Point(0, 1), Point(0, 2), Point(0, 3)])

    def test_same_points(self):
        with self.assertRaises(ValueError):
            list(in_between(Point(), Point()))

    def test_not_horizontal_or_vertical(self):
        with self.assertRaises(ValueError):
            list(in_between(Point(0, 0), Point(1, 1)))


# class SolveTest(unittest.TestCase):
#
#     def test_sample_path(self):
#         self.assertEqual(solve('R8, R4, R4, R8'), 4)
