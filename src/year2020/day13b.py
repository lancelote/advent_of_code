"""2020 - Day 13 Part 2: Shuttle Search."""
from typing import NamedTuple


class Shuttle(NamedTuple):
    i: int
    pk: int


def process_data(data: str) -> list[Shuttle]:
    _, pks = data.strip().split("\n")
    return [
        Shuttle(i, int(pk)) for i, pk in enumerate(pks.split(",")) if pk != "x"
    ]


def find_earliest(shuttles: list[Shuttle]) -> int:
    timestamp = 0
    step = shuttles[0].pk

    for shuttle in shuttles[1:]:
        while (timestamp + shuttle.i) % shuttle.pk != 0:
            timestamp += step

        # prime numbers p1 and p2 repeat their relative position every p1*p2
        step *= shuttle.pk

    return timestamp


def solve(task: str) -> int:
    """Find the closest shuttle."""
    shuttles = process_data(task)
    return find_earliest(shuttles)
