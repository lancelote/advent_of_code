"""2025 - Day 5 Part 1: Cafeteria"""

type Range = tuple[int, int]
type Ingredient = int


def to_range(line: str) -> Range:
    x, y = line.split("-")
    return int(x), int(y)


def process_data(task: str) -> tuple[list[Range], list[Ingredient]]:
    first, second = task.split("\n\n")

    ranges = [to_range(line) for line in first.splitlines()]
    ingredients = [int(line) for line in second.splitlines()]

    return ranges, ingredients


def is_fresh(x: Ingredient, ranges: list[Range]) -> bool:
    for left, right in ranges:
        if left <= x <= right:
            return True
    return False


def solve(task: str) -> int:
    ranges, ingredients = process_data(task)
    return sum(is_fresh(x, ranges) for x in ingredients)
