"""2021 - Day 19 Part 1: Beacon Scanner."""
import pytest

from src.year2021.day19a import Position


@pytest.mark.parametrize(
    "line,position",
    [
        ("645,-448,-766", Position(645, -448, -766)),
        ("0,0,1", Position(0, 0, 1)),
    ],
)
def test_position_from_line(line, position):
    assert Position.from_line(line) == position

