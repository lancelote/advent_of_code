""""Day 12 Part 1: Subterranean Sustainability tests."""

from textwrap import dedent

from src.year2018.day12a import get_pattern, process_data, solve, Pot


def test_process_data():
    test_data = dedent("""
        initial state: .##..

        ##.#. => #
        ##... => #
        #.... => .
    """)
    expected_plants = {
        1: Pot.PLANT,
        2: Pot.PLANT,
    }
    expected_patterns = {
        '##.#.': Pot.PLANT,
        '##...': Pot.PLANT,
        '#....': Pot.EMPTY,
    }

    actual_state, actual_patterns = process_data(test_data)
    assert actual_state == expected_plants
    assert actual_patterns == expected_patterns


def test_get_pattern():
    test_plants = {1: Pot.PLANT, 3: Pot.PLANT}
    assert get_pattern(test_plants, 2) == '.#.#.'


def test_solve():
    test_task = dedent("""
    initial state: #..#.#..##......###...###

    ...## => #
    ..#.. => #
    .#... => #
    .#.#. => #
    .#.## => #
    .##.. => #
    .#### => #
    #.#.# => #
    #.### => #
    ##.#. => #
    ##.## => #
    ###.. => #
    ###.# => #
    ####. => #
    """)
    assert solve(test_task) == 325
