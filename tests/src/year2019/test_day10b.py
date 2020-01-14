from textwrap import dedent

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


def test_big_example():
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
    chart.set_base(x=11, y=13)
    assert chart.remove_till(n=200) == (8, 2)
