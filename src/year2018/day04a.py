"""2018 - Day 4 Part 1: Repose Record."""
from __future__ import annotations

import datetime as dt
import re
from collections import defaultdict
from dataclasses import dataclass
from enum import Enum
from operator import itemgetter
from typing import DefaultDict

RECORD_PATTERN = r"\[(.*)\] (?:(G)uard #(\d+)|(f)|(w))"


class Event(Enum):
    """Possible guard events."""

    NEW = 1  # New guard on duty
    AWAKE = 2  # A guard awakes
    ASLEEP = 3  # A guard falls asleep


@dataclass(frozen=True)
class Record:
    """Guard event record item."""

    time: dt.datetime
    event: Event
    guard: int | None = None  # If new guard is on duty

    @classmethod
    def parse(cls, line: str) -> Record:
        """Convert one line into Event instance."""
        match = re.match(RECORD_PATTERN, line)
        if match:
            stamp, new, guard, asleep, awake = match.groups()
        else:
            raise ValueError("Unknown record format")

        time = dt.datetime.strptime(stamp, "%Y-%m-%d %H:%M")
        if new:
            event = Event.NEW
        elif asleep:
            event = Event.ASLEEP
        elif awake:
            event = Event.AWAKE
        else:
            raise ValueError("Unknown event")

        return cls(time, event, int(guard) if guard else None)

    @classmethod
    def parse_all(cls, data: str) -> list[Record]:
        """Convert a bunch of lines into Record instances."""
        records = [cls.parse(line) for line in data.strip().split("\n")]
        return sorted(records, key=lambda x: x.time)

    @classmethod
    def parse_task(cls, task: str) -> DefaultDict[int, list[int]]:
        """Parse the task into a dict of guard_id: list of minutes."""
        guard, start, end = 0, 0, 0

        minutes: DefaultDict[int, list[int]] = defaultdict(lambda: [0] * 60)
        records = cls.parse_all(task)

        for record in records:
            if record.event == Event.NEW:
                assert record.guard  # Should not be None
                guard = record.guard
            elif record.event == Event.ASLEEP:
                start = record.time.minute
            elif record.event == Event.AWAKE:
                end = record.time.minute
                for minute in range(start, end):
                    minutes[guard][minute] += 1
        return minutes


def total_minutes(guard_minutes: tuple[int, list[int]]) -> int:
    """Sum all sleepy minutes of the given guard."""
    _, minutes = guard_minutes
    return sum(minutes)


def solve(task: str) -> int:
    """Find most sleepy guard and his most sleepy minute value."""
    minutes = Record.parse_task(task)
    guard, _ = max(minutes.items(), key=total_minutes)
    minute, _ = max(enumerate(minutes[guard]), key=itemgetter(1))
    return guard * minute
