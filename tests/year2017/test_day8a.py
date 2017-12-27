"""2017 - Day 8 Part 1: I Heard You Like Registers."""

import pytest

from src.year2017.day8a import process_line, process_data, Instruction, solve


@pytest.mark.parametrize(
    ('line', 'expected'),
    [
        ('b inc 5 if a > 1', Instruction('b', 'inc', 5, 'a', '>', 1)),
        ('a inc 1 if b < 5', Instruction('a', 'inc', 1, 'b', '<', 5)),
        ('c dec -10 if a >= 1', Instruction('c', 'dec', -10, 'a', '>=', 1)),
        ('c inc -20 if c == 10', Instruction('c', 'inc', -20, 'c', '==', 10))
    ]
)
def test_process_line(line, expected):
    assert process_line(line) == expected


def test_process_data():
    data = 'b inc 5 if a > 1\na inc 1 if b < 5\n'
    expected = [Instruction('b', 'inc', 5, 'a', '>', 1),
                Instruction('a', 'inc', 1, 'b', '<', 5)]
    assert process_data(data) == expected


def test_solve():
    data = 'b inc 5 if a > 1\n' \
           'a inc 1 if b < 5\n' \
           'c dec -10 if a >= 1\n' \
           'c inc -20 if c == 10\n'
    assert solve(data) == 1
