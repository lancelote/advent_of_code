"""2015 - Day 6 Part 1: Probably a Fire Hazard."""

import pytest

from src.year2015.day06a import Command, process_data, solve, update_light


@pytest.mark.parametrize(
    "data,expected",
    (
        (
            "turn on 489,959 through 759,964",
            [(Command.TURN_ON, (489, 959), (759, 964))],
        ),
        (
            "turn off 820,516 through 871,914",
            [(Command.TURN_OFF, (820, 516), (871, 914))],
        ),
        (
            "toggle 120,314 through 745,489",
            [(Command.TOGGLE, (120, 314), (745, 489))],
        ),
    ),
)
def test_process_data(data, expected):
    assert process_data(data) == expected


@pytest.mark.parametrize(
    "command,light,expected",
    (
        (Command.TOGGLE, True, 0),
        (Command.TOGGLE, False, 1),
        (Command.TURN_ON, True, 1),
        (Command.TURN_ON, False, 1),
        (Command.TURN_OFF, False, 0),
        (Command.TURN_OFF, True, 0),
    ),
)
def test_update_light(command, light, expected):
    assert update_light(command, light) == expected


@pytest.mark.parametrize(
    "task,expected",
    (
        ("turn on 0,0 through 999,999", 10**6),
        ("toggle 0,0 through 999,0", 1000),
    ),
)
def test_solve(task, expected):
    assert solve(task) == expected
