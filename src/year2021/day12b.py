"""2021 - Day 12 Part 2: Passage Pathing."""
from src.year2021.day12a import Cave
from src.year2021.day12a import parse_task


def visit(cave: Cave, visited1: set[str], visited2: str | None = None) -> int:
    if cave.name == "end":
        return 1
    elif cave.name == "start":
        return 0

    routes = 0

    if cave.is_small and cave.name not in visited1:
        visited1.add(cave.name)
    elif cave.is_small and cave.name in visited1:
        assert visited2 is None
        visited2 = cave.name

    for neighbor in cave.adjacent:
        not_visited1 = neighbor.name not in visited1
        not_visited2 = visited2 is None

        if not neighbor.is_small or not_visited1 or not_visited2:
            routes += visit(neighbor, visited1, visited2)

    if cave.is_small and cave.name != visited2:
        visited1.discard(cave.name)

    return routes


def solve(task: str) -> int:
    caves = parse_task(task)
    return sum(visit(cave, set()) for cave in caves["start"].adjacent)
