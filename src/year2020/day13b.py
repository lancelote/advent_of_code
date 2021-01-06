"""2020 - Day 13 Part 2: Shuttle Search."""
from typing import List
from typing import NamedTuple


class Shuttle(NamedTuple):
    i: int
    pk: int


def process_data(data: str) -> List[Shuttle]:
    _, pks = data.strip().split("\n")
    return [
        Shuttle(i, int(pk)) for i, pk in enumerate(pks.split(",")) if pk != "x"
    ]


def found(biggest: Shuttle, current: int, shuttles: List[Shuttle]) -> bool:
    return all(
        (current + shuttle.i - biggest.i) % shuttle.pk == 0
        for shuttle in shuttles
    )


def find_earliest(shuttles: List[Shuttle]) -> int:
    current = 0
    biggest = max(shuttles, key=lambda x: x.pk)

    while not found(biggest, current, shuttles):
        current += biggest.pk

    return current - biggest.i


def solve(task: str) -> int:
    """Find the closest shuttle."""
    shuttles = process_data(task)
    return find_earliest(shuttles)
