"""2016 - Day 1 Puzzle Part 1 tests."""

import unittest

from src.year2016.day01a import Point
from src.year2016.day01a import processed_data
from src.year2016.day01a import solve
from src.year2016.day01a import update_direction


class UpdateDirectionTest(unittest.TestCase):
    def test_turn_right(self):
        self.assertEqual(update_direction(0, "R"), 1)

    def test_turn_left(self):
        self.assertEqual(update_direction(0, "L"), 3)

    def test_turn_right_to_return_to_north(self):
        self.assertEqual(update_direction(3, "R"), 0)

    def test_turn_left_to_return_to_north(self):
        self.assertEqual(update_direction(1, "L"), 0)

    def test_turn_right_to_south(self):
        self.assertEqual(update_direction(1, "R"), 2)

    def test_turn_left_to_south(self):
        self.assertEqual(update_direction(3, "L"), 2)


class ProcessedDataTest(unittest.TestCase):
    def test_simple_commands(self):
        self.assertEqual(
            processed_data("R3, R1, R4"), [("R", 3), ("R", 1), ("R", 4)]
        )

    def test_long_distance(self):
        self.assertEqual(processed_data("R12, L345"), [("R", 12), ("L", 345)])


class PointTest(unittest.TestCase):
    def setUp(self):
        self.point = Point()

    def test_not_standard_coordinates(self):
        not_zero_point = Point(1, 2)
        self.assertEqual(not_zero_point.x, 1)
        self.assertEqual(not_zero_point.y, 2)

    def test_move_north(self):
        self.point.move(0, 1)
        self.assertEqual(self.point.x, 0)
        self.assertEqual(self.point.y, 1)

    def test_move_east(self):
        self.point.move(1, 1)
        self.assertEqual(self.point.x, 1)
        self.assertEqual(self.point.y, 0)

    def test_move_south(self):
        self.point.move(2, 1)
        self.assertEqual(self.point.x, 0)
        self.assertEqual(self.point.y, -1)

    def test_move_west(self):
        self.point.move(3, 1)
        self.assertEqual(self.point.x, -1)
        self.assertEqual(self.point.y, 0)

    def test_long_distance(self):
        self.point.move(0, 100)
        self.assertEqual(self.point.x, 0)
        self.assertEqual(self.point.y, 100)

    def test_distance_from_zero_pos_pos(self):
        self.assertEqual(Point(1, 2).distance_from_zero(), 3)

    def test_distance_from_zero_pos_neg(self):
        self.assertEqual(Point(2, -3).distance_from_zero(), 5)

    def test_distance_from_zero_neg_neg(self):
        self.assertEqual(Point(-3, -1).distance_from_zero(), 4)

    def test_distance_from_zero_neg_pos(self):
        self.assertEqual(Point(-4, 1).distance_from_zero(), 5)

    def test_distance_from_zero_if_zero(self):
        self.assertEqual(Point().distance_from_zero(), 0)

    def test_repr_representation(self):
        self.assertEqual(repr(self.point), "(0, 0)")
        self.point.move(0, 2)
        self.point.move(1, 1)
        self.assertEqual(repr(self.point), "(1, 2)")

    def test_eq(self):
        self.assertEqual(Point(), Point())
        self.assertEqual(Point(1, 2), Point(1, 2))


class SolveTest(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve("R2, L3"), 5)
        self.assertEqual(solve("R2, R2, R2"), 2)
        self.assertEqual(solve("R5, L5, R5, R3"), 12)
