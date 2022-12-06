"""2022 - Day 6 Part 1: Tuning Trouble."""
import pytest

from src.year2022.day06a import solve


@pytest.mark.parametrize(
    "task,expected",
    [
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
        ("nppdvjthqldpwncqszvftbrmjlhg", 6),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11),
    ],
)
def test_solve(task, expected):
    assert solve(task) == expected
