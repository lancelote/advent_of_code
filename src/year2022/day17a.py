"""2022 - Day 17 Part 1: Pyroclastic Flow."""
from __future__ import annotations

from abc import ABC
from abc import abstractmethod
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
class Piece(ABC):
    left: int
    bottom: int
    rocks: Rocks
    landed: bool = False

    def __init__(self, left: int, bottom: int) -> None:
        self.left = left
        self.bottom = bottom

    @classmethod
    def from_form(cls, form: Form, left: int, bottom: int) -> Piece:
        match form:
            case Form.MINUS:
                return MinusPiece(left, bottom)
            case Form.PLUS:
                return PlusPiece(left, bottom)
            case Form.CORNER:
                return CornerPiece(left, bottom)
            case Form.VERTICAL:
                return VerticalPiece(left, bottom)
            case Form.SQUARE:
                return SquarePiece(left, bottom)
            case _:
                raise NotImplementedError

    def commit(self, fallen_rocks: Rocks) -> None:
        fallen_rocks.update(self.rocks)

    def can_be_pushed(self, fallen_rocks: Rocks) -> bool:
        raise NotImplementedError

    @abstractmethod
    def push(self, jet: Jet, rocks: Rocks) -> None:
        raise NotImplementedError

    @abstractmethod
    def can_fall(self, fallen_rocks: Rocks) -> bool:
        raise NotImplementedError

    @abstractmethod
    def fall(self, fallen_rocks: Rocks) -> None:
        if not self.can_fall(fallen_rocks):
            self.landed = True
        else:
            self.rocks = {(x, y - 1) for (x, y) in self.rocks}


class MinusPiece(Piece):
    def __init__(self, left: int, bottom: int) -> None:
        super().__init__(left, bottom)
        self.rocks = {
            (left, bottom),
            (left + 1, bottom),
            (left + 2, bottom),
            (left + 3, bottom),
        }


class PlusPiece(Piece):
    pass


class CornerPiece(Piece):
    pass


class VerticalPiece(Piece):
    pass


class SquarePiece(Piece):
    pass


def solve(task: str) -> int:
    top = 0
    fallen_rocks: Rocks = set()

    forms = iterate_forms()
    jets = iterate_jets(task)

    for _ in range(2022):
        piece = Piece.from_form(next(forms), left=2, bottom=top + 3)

        while not piece.landed:
            jet = next(jets)

            piece.push(jet, fallen_rocks)
            piece.fall(fallen_rocks)

        top = piece.bottom
        piece.commit(fallen_rocks)

    return top
