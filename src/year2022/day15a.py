"""2022 - Day 15 Part 1: Beacon Exclusion Zone."""
from __future__ import annotations

import re
from dataclasses import dataclass
from typing import NamedTuple


class Section(NamedTuple):
    x1: int
    x2: int


class Beacon(NamedTuple):
    x: int
    y: int


@dataclass
class Sensor:
    x: int
    y: int
    beacon: Beacon

    @property
    def distance(self) -> int:
        return abs(self.x - self.beacon.x) + abs(self.y - self.beacon.y)

    @classmethod
    def from_line(cls, line: str) -> Sensor:
        x1, y1, x2, y2 = (int(x) for x in re.findall(r"[\-\d]+", line))
        beacon = Beacon(x2, y2)
        sensor = Sensor(x1, y1, beacon)
        return sensor


def get_section(y: int, sensor: Sensor) -> Section:
    x1, x2 = 0, 0

    diff = sensor.distance - abs(sensor.y - y)

    if diff >= 0:
        x1 = sensor.x - diff
        x2 = sensor.x + diff

    return Section(x1, x2)


def merge_sections(sections: list[Section]) -> list[Section]:
    sections = sorted(sections)
    merged_sections: list[Section] = []
    start, end = sections[0]

    for i in range(1, len(sections)):
        x1, x2 = sections[i]

        if x1 <= end:
            end = max(end, x2)
        else:
            merged_sections.append(Section(start, end))
            start, end = x1, x2

    merged_sections.append(Section(start, end))
    return merged_sections


def solve(task: str, y: int = 2_000_000) -> int:
    sensors = [Sensor.from_line(line) for line in task.splitlines()]
    sections = [get_section(y, sensor) for sensor in sensors]
    sections = merge_sections(sections)
    return sum(section.x2 - section.x1 for section in sections)
