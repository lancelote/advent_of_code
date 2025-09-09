"""2015 - Day 14 Part 1: Reindeer Olympics."""

import re
from dataclasses import dataclass
from typing import Self


@dataclass
class Reindeer:
    speed: int
    travel_time: int
    rest_time: int

    @classmethod
    def from_string(cls, line: str) -> Self:
        match: list[str] = re.findall(r"(\d+)", line)
        assert len(match) == 3

        a, b, c = match
        return cls(int(a), int(b), int(c))

    def distance_after(self, seconds: int) -> int:
        total_cycles = seconds // (self.travel_time + self.rest_time)
        left_time = seconds % (self.travel_time + self.rest_time)

        result = total_cycles * (self.travel_time * self.speed)

        if left_time < self.travel_time:
            result += left_time * self.speed
        else:
            result += self.travel_time * self.speed

        return result


def process_data(data: str) -> list[Reindeer]:
    return [Reindeer.from_string(line) for line in data.splitlines()]


def solve(task: str) -> int:
    deers = process_data(task)
    return max(deer.distance_after(2503) for deer in deers)
