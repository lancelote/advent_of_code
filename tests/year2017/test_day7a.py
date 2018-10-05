"""2017 - Day 7 Part 1: Recursive Circus tests."""

import pytest

from src.year2017.day7a import solve, process_line, process_data, find_root


@pytest.mark.parametrize(
    ('line', 'expected'),
    [
        ('pbga (66)', ('pbga', 66, [])),
        ('abcdefg (12345)', ('abcdefg', 12345, [])),
        ('fwft (72) -> ktlj, cntj', ('fwft', 72, ['ktlj', 'cntj']))
    ]
)
def test_process_line(line, expected):
    assert process_line(line) == expected


def test_process_line_wrong_command_format():
    with pytest.raises(ValueError, match='Wrong command format'):
        process_line('hello world')


def test_process_line_wrong_weight_format():
    with pytest.raises(ValueError, match='Wrong command format'):
        process_line('pbga (hello)')


def test_process_data():
    data = """
    jptl (61)
    ugml (68) -> gyxo, ebii, jptl
    """
    expected = [
        ('jptl', 61, []),
        ('ugml', 68, ['gyxo', 'ebii', 'jptl']),
    ]
    assert process_data(data) == expected


@pytest.mark.parametrize(
    ('tree', 'expected'),
    [
        ({'b': 'a', 'c': 'a', 'a': None}, 'a'),
        ({'b': 'a', 'a': 'b'}, None),
        ({'d': 'b', 'b': 'a', 'a': None, 'c': 'a'}, 'a')
    ]
)
def test_find_root(tree, expected):
    assert find_root(tree) == expected


def test_solve():
    data = """
    pbga (66)
    xhth (57)
    ebii (61)
    havc (66)
    ktlj (57)
    fwft (72) -> ktlj, cntj, xhth
    qoyq (66)
    padx (45) -> pbga, havc, qoyq
    tknk (41) -> ugml, padx, fwft
    jptl (61)
    ugml (68) -> gyxo, ebii, jptl
    gyxo (61)
    cntj (57)
    """
    assert solve(data) == 'tknk'
