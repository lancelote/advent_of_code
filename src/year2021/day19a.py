"""2021 - Day 19 Part 1: Beacon Scanner."""
from __future__ import annotations

import re
from dataclasses import dataclass
from typing import NamedTuple
from typing import Iterator

DETECTION_RANGE = 1_000
BEACONS_TO_MATCH = 12


class Position(NamedTuple):
    x: int
    y: int
    z: int

    @classmethod
    def from_line(cls, line: str) -> Position:
        a, b, c = line.split(",")
        return Position(int(a), int(b), int(c))


@dataclass
class Scanner:
    pk: int
    signatures: list[Position]
    absolute_position: Position | None = None

    @classmethod
    def from_text(cls, text: str) -> Scanner:
        [header, *body] = text.splitlines()
        [pk_str] = re.findall(r"\d+", header)
        pk = int(pk_str)
        beacons = [Position.from_line(line) for line in body]
        return Scanner(pk, beacons)

    def beacons(self) -> Iterator[Position]:
        assert isinstance(self.absolute_position, Position)
        x, y, z = self.absolute_position

        for dx, dy, dz in self.signatures:
            yield Position(x + dx, y + dy, z + dz)


def triangulate_rest(first: Scanner, rest: list[Scanner]) -> None:
    to_compare_with = [first]

    while rest:
        known_scanner = to_compare_with.pop()
        no_overlaps = []

        for unknown_scanner in rest:
            if known_scanner.overlap(unknown_scanner):
                unknown_scanner.triangulate_by(known_scanner)
                to_compare_with.append(unknown_scanner)
            else:
                no_overlaps.append(unknown_scanner)

        rest = no_overlaps


def unique_beacons(scanners: list[Scanner]) -> set[Position]:
    return {
        beacon
        for scanner in scanners
        for beacon in scanner.beacons()
    }


def solve(task: str) -> int:
    scanners = [Scanner.from_text(text) for text in task.split("\n\n")]
    [first, *rest] = scanners
    first.absolute_position = Position(0, 0, 0)
    triangulate_rest(first, rest)
    beacons = unique_beacons(scanners)
    return len(beacons)
