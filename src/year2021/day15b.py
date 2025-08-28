"""2021 - Day 15 Part 2: Chiton."""

from src.year2021.day15a import Point, RiskMap, walk


def solve(task: str) -> int:
    risk_map = RiskMap.from_task_b(task)

    start = Point(0, 0)
    target = Point(risk_map.max_x, risk_map.max_y)

    return walk(start, target, risk_map)
