"""Day 12 Part 1: Subterranean Sustainability tests."""

from textwrap import dedent

import pytest

from src.year2018.day12a import (
    Pot,
    get_new_generation,
    get_pattern,
    process_data,
    solve,
)


@pytest.fixture
def task():
    return dedent(
        """
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
    """
    )


def test_process_data():
    test_data = dedent(
        """
        initial state: .##..

        ##.#. => #
        ##... => #
        #.... => .
    """
    )
    expected_plants = {
        1: Pot.PLANT,
        2: Pot.PLANT,
    }
    expected_patterns = {
        "##.#.": Pot.PLANT,
        "##...": Pot.PLANT,
        "#....": Pot.EMPTY,
    }

    actual_state, actual_patterns = process_data(test_data)
    assert actual_state == expected_plants
    assert actual_patterns == expected_patterns


def test_get_pattern():
    test_plants = {1: Pot.PLANT, 3: Pot.PLANT}
    assert get_pattern(test_plants, 2) == ".#.#."


def test_solve(task):
    assert solve(task) == 325


def test_get_new_generation(task):
    generation, patterns = process_data(task)

    new_generation = get_new_generation(generation, patterns)
    expected_generation = {
        0: Pot.PLANT,
        4: Pot.PLANT,
        9: Pot.PLANT,
        15: Pot.PLANT,
        18: Pot.PLANT,
        21: Pot.PLANT,
        24: Pot.PLANT,
    }
    assert new_generation == expected_generation
