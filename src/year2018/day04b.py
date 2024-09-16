"""2018 - Day 4 Part 1: Repose Record."""

from operator import itemgetter

from src.year2018.day04a import Record


def most_sleepy(guard_minutes: tuple[int, list[int]]) -> int:
    """Find most sleepy minute value."""
    _, minutes = guard_minutes
    return max(minutes)


def solve(task: str) -> int:
    """Find the most sleepy minute by guard."""
    minutes = Record.parse_task(task)
    guard, guard_minutes = max(minutes.items(), key=most_sleepy)
    minute, _ = max(enumerate(guard_minutes), key=itemgetter(1))
    return guard * minute
