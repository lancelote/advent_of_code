"""2018 - Day 4 Part 1: Repose Record.

Strategy 2: Of all guards, which guard is most frequently asleep on the same
minute?

In the example above, Guard #99 spent minute 45 asleep more than any other
guard or minute - three times in total. (In all other cases, any guard spent
any minute asleep at most twice.)

What is the ID of the guard you chose multiplied by the minute you chose? (In
the above example, the answer would be 99 * 45 = 4455.)
"""
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
