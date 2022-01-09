"""2021 - Day 19 Part 1: Beacon Scanner."""
from textwrap import dedent

import pytest

from src.year2021.day19a import Position
from src.year2021.day19a import Scanner


@pytest.mark.parametrize(
    "line,position",
    [
        ("645,-448,-766", Position(645, -448, -766)),
        ("0,0,1", Position(0, 0, 1)),
    ],
)
def test_position_from_line(line, position):
    assert Position.from_line(line) == position


def test_scanner_from_text():
    text = dedent("""
        --- scanner 0 ---
        645,-448,-766
        529,751,-867
    """).strip()
    actual_scanner = Scanner.from_text(text)
    expected_scanner = Scanner(
        pk=0,
        signatures=[
            Position(645, -448, -766),
            Position(529, 751, -867),
        ]
    )
    assert actual_scanner == expected_scanner
