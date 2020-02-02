"""2019 - Day 14 Part 1: Space Stoichiometry tests."""

from textwrap import dedent

from src.year2019.day14a import process_data, Chemical, Reaction


def test_process_data():
    data = dedent("""
        10 ORE => 10 A
        1 ORE => 1 B
        7 A, 1 B => 1 C
        7 A, 1 C => 1 D
        7 A, 1 D => 1 E
        7 A, 1 E => 1 FUEL
    """)
    expected = {
        'A': Reaction(10, [Chemical(10, 'ORE'),]),
        'B': Reaction(1, [Chemical(1, 'ORE'),]),
        'C': Reaction(1, [Chemical(7, 'A'), Chemical(1, 'B'),]),
        'D': Reaction(1, [Chemical(7, 'A'), Chemical(1, 'C'),]),
        'E': Reaction(1, [Chemical(7, 'A'), Chemical(1, 'D'),]),
        'FUEL': Reaction(1, [Chemical(7, 'A'), Chemical(1, 'E'),]),
    }
    assert process_data(data) == expected
