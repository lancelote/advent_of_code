"""2019 - Day 8 Part 1: Space Image Format tests."""

from src.year2019.day08a import parse_layers


def test_parse_layers():
    data = "123456789012"
    assert parse_layers(data, 6) == [
        [1, 2, 3, 4, 5, 6],
        [7, 8, 9, 0, 1, 2],
    ]
