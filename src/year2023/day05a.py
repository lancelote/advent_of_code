"""2023 - Day 5 Part 1: If You Give A Seed A Fertilizer"""

from dataclasses import dataclass
from typing import Self


@dataclass
class Range:
    dest_start: int
    src_start: int
    length: int

    @classmethod
    def from_line(cls, line: str) -> Self:
        # e.g., "50 98 2"
        dest_part, src_part, len_part = line.split()
        dest_start = int(dest_part)
        src_start = int(src_part)
        length = int(len_part)
        return cls(dest_start, src_start, length)

    def get(self, key: int) -> int:
        return key - self.src_start + self.dest_start

    def __contains__(self, key: int) -> bool:
        return self.src_start <= key < (self.src_start + self.length)


@dataclass
class Map:
    src: str
    dest: str
    ranges: list[Range]

    @classmethod
    def from_text(cls, text: str) -> Self:
        # e.g., seed-to-soil map:
        #       50 98 2
        #       52 50 48
        lines = text.splitlines()
        keys_part, _ = lines[0].split(" ")
        src, _, dest = keys_part.split("-")
        ranges = [Range.from_line(lines[i]) for i in range(1, len(lines))]
        return cls(src, dest, ranges)

    def get(self, key: int) -> int:
        for r in self.ranges:
            if key in r:
                return r.get(key)
        return key


def get_location(seed: int, maps: dict[str, Map]) -> int:
    # seed > soil > fertilizer > water >
    #   light > temperature > humidity > location

    soil = maps["soil"].get(seed)
    fertilizer = maps["fertilizer"].get(soil)
    water = maps["water"].get(fertilizer)
    light = maps["light"].get(water)
    temperature = maps["temperature"].get(light)
    humidity = maps["humidity"].get(temperature)
    location = maps["location"].get(humidity)

    return location


def process_data(task: str) -> tuple[list[int], dict[str, Map]]:
    blocks = task.split("\n\n")
    _, seeds_part = blocks[0].split(": ")
    seeds = [int(x) for x in seeds_part.split(" ")]
    maps = [Map.from_text(blocks[i]) for i in range(1, len(blocks))]
    return seeds, {m.dest: m for m in maps}


def solve(task: str) -> int:
    seeds, maps = process_data(task)
    return min(get_location(x, maps) for x in seeds)
