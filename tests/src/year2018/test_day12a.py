""""Day 12 Part 1: Subterranean Sustainability tests."""

from collections import defaultdict
from textwrap import dedent

from src.year2018.day12a import process_data, get_pattern


def test_process_data():
    test_data = dedent("""
        initial state: .##..

        ##.#. => #
        ##... => #
        #.... => .
    """)
    expected_state = {
        -5: '.',
        -4: '.',
        -3: '.',
        -2: '.',
        -1: '.',
        0: '.',
        1: '#',
        2: '#',
        3: '.',
        4: '.',
    }
    expected_state.update({i: '.' for i in range(5, 35)})
    expected_patterns = {
        '##.#.': '#',
        '##...': '#',
        '#....': '.'
    }

    actual_state, actual_patterns, length = process_data(test_data)
    assert dict(actual_state) == expected_state
    assert dict(actual_patterns) == expected_patterns
    assert length == 5


def test_get_pattern():
    test_state = defaultdict(lambda: '.', {
        0: '.',
        1: '#',
        2: '.',
        3: '#',
        4: '.'
    })
    assert get_pattern(test_state, 2) == '.#.#.'
