"""2019 - Day 10 Part 2: Monitoring Station tests."""

from textwrap import dedent

import pytest

from src.year2019.day10b import Chart


def test_simple_case():
    task = dedent("""
    ###
    ###
    ###
    """)
    chart = Chart.from_string(task)
    chart.set_base(x=1, y=1)
    assert chart.remove_till(n=1) == (1, 0)


def test_small_example():
    task = dedent("""
        .#....#####...#..
        ##...##.#####..##
        ##...#...#.#####.
        ..#.....#...###..
        ..#.#.....#....##
    """)
    chart = Chart.from_string(task)
    chart.set_base(x=8, y=3)
    assert chart.remove_till(n=1) == (8, 1)


@pytest.mark.parametrize('n,x,y', [
    (1, 11, 12),
    (2, 12, 1),
    (3, 12, 2),
    (10, 12, 8),
    (20, 16, 0),
    (50, 16, 9),
    (100, 10, 16),
    (199, 9, 6),
    (200, 8, 2),
    (201, 10, 9),
    (299, 11, 1),
])
def test_big_example(n, x, y):
    task = dedent("""
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
    """)
    chart = Chart.from_string(task)
    _, station_x, station_y = chart.optimal_station_position

    assert station_x == 11
    assert station_y == 13

    chart.set_base(station_x, station_y)

    assert chart.remove_till(n) == (x, y)
