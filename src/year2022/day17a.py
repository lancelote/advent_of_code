"""2022 - Day 17 Part 1: Pyroclastic Flow."""
from collections.abc import Iterator
from dataclasses import dataclass
from enum import Enum
from typing import TypeAlias

Rocks: TypeAlias = set[tuple[int, int]]


class Jet(Enum):
    LEFT = "<"
    RIGHT = ">"


def iterate_jets(task: str) -> Iterator[Jet]:
    while True:
        for x in task:
            yield Jet(x)


class Form(Enum):
    MINUS = 0
    PLUS = 1
    CORNER = 2
    VERTICAL = 3
    SQUARE = 4


def iterate_forms() -> Iterator[Form]:
    while True:
        yield from Form


@dataclass
class Piece:
    form: Form
    left: int
    bottom: int
    landed: bool = False

    def push(self, jet: Jet, rocks: Rocks) -> None:
        raise NotImplementedError

    def fall(self, rocks: Rocks) -> None:
        raise NotImplementedError


def solve(task: str) -> int:
    top = 0
    rocks: Rocks = set()

    forms = iterate_forms()
    jets = iterate_jets(task)

    for _ in range(2022):
        piece = Piece(form=next(forms), left=2, bottom=top + 3)

        while not piece.landed:
            jet = next(jets)

            piece.push(jet, rocks)
            piece.fall(rocks)

    return top
