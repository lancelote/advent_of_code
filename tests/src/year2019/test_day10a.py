"""2019 - Day 10 Part 1: Monitoring Station tests."""

from textwrap import dedent

import pytest

from src.year2019.day10a import Chart


@pytest.fixture
def simple_task():
    return dedent(
        """
        .#..#
        .....
        #####
        ....#
        ...##
        """
    )


@pytest.fixture
def simple_chart(simple_task):
    return Chart.from_string(simple_task)


def test_from_string(simple_task):
    chart = Chart.from_string(simple_task)

    assert chart.locations == [
        [False, True, False, False, True],
        [False, False, False, False, False],
        [True, True, True, True, True],
        [False, False, False, False, True],
        [False, False, False, True, True],
    ]


@pytest.mark.parametrize(
    "x,y,expected",
    [
        (1, 0, 7),
        (4, 0, 7),
        (0, 2, 6),
        (1, 2, 7),
        (2, 2, 7),
        (3, 2, 7),
        (4, 2, 5),
        (4, 3, 7),
        (3, 4, 8),
        (4, 4, 7),
    ],
)
def test_count_visible_asteroids(x, y, expected, simple_chart):
    assert simple_chart.seen_from(x, y) == expected


def test_most_observant(simple_chart):
    assert simple_chart.most_observant == 8


@pytest.mark.parametrize(
    "example,expected",
    [
        (
            dedent(
                """
                ......#.#.
                #..#.#....
                ..#######.
                .#.#.###..
                .#..#.....
                ..#....#.#
                #..#....#.
                .##.#..###
                ##...#..#.
                .#....####
                """
            ),
            33,
        ),
        (
            dedent(
                """
                #.#...#.#.
                .###....#.
                .#....#...
                ##.#.#.#.#
                ....#.#.#.
                .##..###.#
                ..#...##..
                ..##....##
                ......#...
                .####.###.
                """
            ),
            35,
        ),
        (
            dedent(
                """
                .#..#..###
                ####.###.#
                ....###.#.
                ..###.##.#
                ##.##.#.#.
                ....###..#
                ..#.#..#.#
                #..#.#.###
                .##...##.#
                .....#.#..
                """
            ),
            41,
        ),
        (
            dedent(
                """
                .#..##.###...#######
                ##.############..##.
                .#.######.########.#
                .###.#######.####.#.
                #####.##.#.##.###.##
                ..#####..#.#########
                ####################
                #.####....###.#.#.##
                ##.#################
                #####.##.###..####..
                ..######..##.#######
                ####.##.####...##..#
                .#####..#.######.###
                ##...#.##########...
                #.##########.#######
                .####.#.###.###.#.##
                ....##.##.###..#####
                .#.#.###########.###
                #.#.#.#####.####.###
                ###.##.####.##.#..##
                """
            ),
            210,
        ),
    ],
)
def test_most_observant_large_examples(example, expected):
    assert Chart.from_string(example).most_observant == expected
