"""2018 - Day 4 Part 1: Repose Record tests."""

import datetime as dt
from textwrap import dedent

import pytest

from src.year2018.day4a import Event, Record, solve, total_minutes


@pytest.mark.parametrize(
    ('line', 'expected'),
    [
        (
                '[1518-05-16 00:00] Guard #1319 begins shift',
                Record(dt.datetime(1518, 5, 16, 0, 0), Event.NEW, 1319)
        ),
        (
                '[1518-03-24 00:50] wakes up',
                Record(dt.datetime(1518, 3, 24, 0, 50), Event.AWAKE)
        ),
        (
                '[1518-08-18 00:42] falls asleep',
                Record(dt.datetime(1518, 8, 18, 0, 42), Event.ASLEEP)
        ),
        (
                '[1518-05-11 00:03] Guard #163 begins shift',
                Record(dt.datetime(1518, 5, 11, 0, 3), Event.NEW, 163)
        )
    ]
)
def test_parse(line, expected):
    assert Record.parse(line) == expected


def test_parse_all():
    data = dedent("""
        [1518-05-16 00:00] Guard #1319 begins shift
        [1518-03-24 00:50] wakes up
        [1518-08-18 00:42] falls asleep
    """)
    expected = [
        Record(dt.datetime(1518, 3, 24, 0, 50), Event.AWAKE),
        Record(dt.datetime(1518, 5, 16, 0, 0), Event.NEW, 1319),
        Record(dt.datetime(1518, 8, 18, 0, 42), Event.ASLEEP),
    ]
    assert Record.parse_all(data) == expected


def test_total_minutes():
    assert total_minutes((0, [1, 2, 3])) == 6


def test_solve():
    test_task = dedent("""
        [1518-11-01 00:00] Guard #10 begins shift
        [1518-11-01 00:05] falls asleep
        [1518-11-01 00:25] wakes up
        [1518-11-01 00:30] falls asleep
        [1518-11-01 00:55] wakes up
        [1518-11-01 23:58] Guard #99 begins shift
        [1518-11-02 00:40] falls asleep
        [1518-11-02 00:50] wakes up
        [1518-11-03 00:05] Guard #10 begins shift
        [1518-11-03 00:24] falls asleep
        [1518-11-03 00:29] wakes up
        [1518-11-04 00:02] Guard #99 begins shift
        [1518-11-04 00:36] falls asleep
        [1518-11-04 00:46] wakes up
        [1518-11-05 00:03] Guard #99 begins shift
        [1518-11-05 00:45] falls asleep
        [1518-11-05 00:55] wakes up
    """)
    assert solve(test_task) == 240
