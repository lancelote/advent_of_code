"""Day 12 Part 2: Subterranean Sustainability tests."""

from textwrap import dedent

from src.year2018.day12b import Farm


def test_from_task():
    sample_task = dedent("""
        initial state: .##..
    
        .##.# => #
        ##.#. => #
        ##... => #
        #.... => .
        .#..# => .
    """)
    farm = Farm.from_task(sample_task)
    assert farm.state == {0: '.', 1: '#', 2: '#', 3: '.', 4: '.'}
    assert farm.patterns == {
        '.##.#': '#',
        '##.#.': '#',
        '##...': '#',
        '#....': '.',
        '.#..#': '.',
    }
