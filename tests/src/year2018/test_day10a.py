"""2018 - Day 10 Part 1: The Stars Align tests."""

from textwrap import dedent

import pytest

from src.year2018.day10a import Point, Sky


class TestPoint:
    @pytest.mark.parametrize(
        ("line", "point"),
        [
            (
                "position=< -9875,  -9913> velocity=< 1,  1>",
                Point(x=-9875, y=-9913, dx=1, dy=1),
            ),
            (
                "position=< 40550,  50600> velocity=<-4, -5>",
                Point(x=40550, y=50600, dx=-4, dy=-5),
            ),
            (
                "position=<-50240,  30431> velocity=< 5, -3>",
                Point(x=-50240, y=30431, dx=5, dy=-3),
            ),
            (
                "position=<10, -3> velocity=<-1,  1>",
                Point(x=10, y=-3, dx=-1, dy=1),
            ),
        ],
    )
    def test_from_line(self, line, point):
        assert Point.from_line(line) == point

    def test_parse_task(self):
        task = dedent(
            """
            position=< -9901, -50255> velocity=< 1,  5>
            position=<-50219,  -9916> velocity=< 5,  1>
            position=< 40524, -30086> velocity=<-4,  3>
        """
        )
        expected = [
            Point(-9901, -50255, 1, 5),
            Point(-50219, -9916, 5, 1),
            Point(40524, -30086, -4, 3),
        ]
        assert Point.parse_task(task) == expected

    @pytest.mark.parametrize(
        ("point", "expected_x", "expected_y"),
        [
            (Point(0, 0, 1, 1), 1, 1),
            (Point(5, 4, 1, 1), 6, 5),
            (Point(0, 0, 1, -1), 1, -1),
        ],
    )
    def test_move(self, point, expected_x, expected_y):
        point.move()
        assert point.x == expected_x
        assert point.y == expected_y


def test_iterate_till_min_area():
    task = dedent(
        """
        position=< 9,  1> velocity=< 0,  2>
        position=< 7,  0> velocity=<-1,  0>
        position=< 3, -2> velocity=<-1,  1>
        position=< 6, 10> velocity=<-2, -1>
        position=< 2, -4> velocity=< 2,  2>
        position=<-6, 10> velocity=< 2, -2>
        position=< 1,  8> velocity=< 1, -1>
        position=< 1,  7> velocity=< 1,  0>
        position=<-3, 11> velocity=< 1, -2>
        position=< 7,  6> velocity=<-1, -1>
        position=<-2,  3> velocity=< 1,  0>
        position=<-4,  3> velocity=< 2,  0>
        position=<10, -3> velocity=<-1,  1>
        position=< 5, 11> velocity=< 1, -2>
        position=< 4,  7> velocity=< 0, -1>
        position=< 8, -2> velocity=< 0,  1>
        position=<15,  0> velocity=<-2,  0>
        position=< 1,  6> velocity=< 1,  0>
        position=< 8,  9> velocity=< 0, -1>
        position=< 3,  3> velocity=<-1,  1>
        position=< 0,  5> velocity=< 0, -1>
        position=<-2,  2> velocity=< 2,  0>
        position=< 5, -2> velocity=< 1,  2>
        position=< 1,  4> velocity=< 2,  1>
        position=<-2,  7> velocity=< 2, -2>
        position=< 3,  6> velocity=<-1, -1>
        position=< 5,  0> velocity=< 1,  0>
        position=<-6,  0> velocity=< 2,  0>
        position=< 5,  9> velocity=< 1, -2>
        position=<14,  7> velocity=<-2,  0>
        position=<-3,  6> velocity=< 2, -1>
    """
    )
    points = Point.parse_task(task)
    sky = Sky(points)
    sky.move_till_min_area()
    min_x, max_x, min_y, max_y = sky.bounds()

    assert min_x == 0
    assert max_x == 9
    assert min_y == 0
    assert max_y == 7
