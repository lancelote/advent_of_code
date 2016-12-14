# pylint: disable=missing-docstring, invalid-name

"""
2016 - Day 1 Puzzle Part 1 tests
"""

import unittest

from src.year2016.day1a import solve, processed_data, update_direction, \
    calculate_distance, update_coordinates


class UpdateDirectionTest(unittest.TestCase):

    def test_turn_right(self):
        self.assertEqual(update_direction(0, 'R'), 1)

    def test_turn_left(self):
        self.assertEqual(update_direction(0, 'L'), 3)

    def test_turn_right_to_return_to_north(self):
        self.assertEqual(update_direction(3, 'R'), 0)

    def test_turn_left_to_return_to_north(self):
        self.assertEqual(update_direction(1, 'L'), 0)

    def test_turn_right_to_south(self):
        self.assertEqual(update_direction(1, 'R'), 2)

    def test_turn_left_to_south(self):
        self.assertEqual(update_direction(3, 'L'), 2)


class ProcessedDataTest(unittest.TestCase):

    def test_simple_commands(self):
        self.assertEqual(
            processed_data('R3, R1, R4'),
            [('R', 3), ('R', 1), ('R', 4)]
        )

    def test_long_distance(self):
        self.assertEqual(
            processed_data('R12, L345'),
            [('R', 12), ('L', 345)]
        )


class CalculateDistanceTest(unittest.TestCase):

    def test_positive_positive(self):
        self.assertEqual(calculate_distance((1, 1)), 2)

    def test_positive_negative(self):
        self.assertEqual(calculate_distance((1, -1)), 2)

    def test_negative_positive(self):
        self.assertEqual(calculate_distance((-1, 1)), 2)

    def test_negative_negative(self):
        self.assertEqual(calculate_distance((-1, -1)), 2)

    def test_zero_zero(self):
        self.assertEqual(calculate_distance((0, 0)), 0)


class UpdateCoordinates(unittest.TestCase):

    def test_north(self):
        self.assertEqual(update_coordinates((0, 0), 0, 1), (0, 1))

    def test_east(self):
        self.assertEqual(update_coordinates((0, 0), 1, 1), (1, 0))

    def test_south(self):
        self.assertEqual(update_coordinates((0, 0), 2, 1), (0, -1))

    def test_west(self):
        self.assertEqual(update_coordinates((0, 0), 3, 1), (-1, 0))

    def test_long_distance(self):
        self.assertEqual(update_coordinates((0, 0), 0, 100), (0, 100))


class SolveTest(unittest.TestCase):

    def test_solve(self):
        self.assertEqual(solve('R2, L3'), 5)
        self.assertEqual(solve('R2, R2, R2'), 2)
        self.assertEqual(solve('R5, L5, R5, R3'), 12)
