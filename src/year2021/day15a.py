"""2021 - Day 15 Part 1: Chiton."""
from __future__ import annotations

from typing import Iterator
from typing import NamedTuple

SHIFTS = {
    (0, -1),
    (+1, 0),
    (0, +1),
    (-1, 0),
}


class RiskMap:
    def __init__(self, data: list[list[int]]):
        self.data = data

    @classmethod
    def from_task(cls, task: str) -> RiskMap:
        data = [[int(x) for x in line] for line in task.splitlines()]
        return cls(data)

    @property
    def max_x(self) -> int:
        assert len(self.data)
        assert len(self.data[0])
        return len(self.data[0]) - 1

    @property
    def max_y(self) -> int:
        assert len(self.data)
        return len(self.data) - 1

    def __getitem__(self, item: Point) -> int:
        return self.data[item.y][item.x]

    def adjacent(self, point: Point) -> Iterator[Point]:
        for dx, dy in SHIFTS:
            new_x = point.x + dx
            new_y = point.y + dy

            valid_new_x = 0 <= new_x < len(self.data[0])
            valid_new_y = 0 <= new_y < len(self.data)

            if valid_new_x and valid_new_y:
                yield Point(new_x, new_y)


class Point(NamedTuple):
    x: int
    y: int


def walk(start: Point, target: Point, risk_map: RiskMap) -> int:
    cumulative_risk = {start: 0}
    to_visit: set[Point] = set()
    to_visit.add(start)

    while to_visit:
        current = to_visit.pop()
        current_path_risk = cumulative_risk[current]

        for point in risk_map.adjacent(current):
            self_risk = risk_map[point]
            candidate_path_risk = current_path_risk + self_risk

            if (
                point not in cumulative_risk
                or cumulative_risk[point] > candidate_path_risk
            ):
                cumulative_risk[point] = candidate_path_risk
                to_visit.add(point)

    return cumulative_risk[target]


def solve(task: str) -> int:
    risk_map = RiskMap.from_task(task)

    start = Point(0, 0)
    target = Point(risk_map.max_x, risk_map.max_y)

    return walk(start, target, risk_map)
