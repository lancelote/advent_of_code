""""Day 13 Part 1: Mine Cart Madness tests."""

import pytest

from src.year2018.day13a import Track


@pytest.fixture
def task():
    return r"""/->-\        
|   |  /----\
| /-+--+-\  |
| | |  | v  |
\-+-/  \-+--/
  \------/   """


def test_track_creation(task):
    expected_grid = [
        ['/', '-', '>', '-', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['|', ' ', ' ', ' ', '|', ' ', ' ', '/', '-', '-', '-', '-', '\\'],
        ['|', ' ', '/', '-', '+', '-', '-', '+', '-', '\\', ' ', ' ', '|'],
        ['|', ' ', '|', ' ', '|', ' ', ' ', '|', ' ', 'v', ' ', ' ', '|'],
        ['\\', '-', '+', '-', '/', ' ', ' ', '\\', '-', '+', '-', '-', '/'],
        [' ', ' ', '\\', '-', '-', '-', '-', '-', '-', '/', ' ', ' ', ' '],
    ]
    track = Track.from_raw_data(task)
    assert track.grid == expected_grid
