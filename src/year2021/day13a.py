"""2021 - Day 13 Part 1: Transparent Origami."""
from __future__ import annotations
from enum import Enum
from typing import NamedTuple


class Point(NamedTuple):
    x: int
    y: int

    @classmethod
    def from_line(cls, line: str) -> Point:
        raw_x, raw_y = line.split(",")
        return Point(
            x=int(raw_x),
            y=int(raw_y)
        )

    def __str__(self) -> str:
        return f"Point({self.x}, {self.y})"

    __repr__ = __str__


class Fold(Enum):
    UP = "y"
    LEFT = "x"


class Paper:
    def __init__(self, data: set[Point]) -> None:
        self.points = data

    @classmethod
    def from_text(cls, text: str) -> Paper:
        return Paper({Point.from_line(line) for line in text.splitlines()})

    @property
    def visible_points(self):
        return len(self.points)

    def fold(self, instruction: Instruction) -> None:
        if instruction.fold is Fold.UP:
            self.fold_up(instruction.position)
        elif instruction.fold is Fold.LEFT:
            self.fold_left(instruction.position)
        else:
            raise ValueError(f"unknown fold: {instruction.fold}")

    def fold_up(self, position: int) -> None:
        left_points = set()

        for point in self.points:
            if point.y < position:
                left_points.add(point)
            elif point.y > position:
                new_point = Point(point.x, 2*position - point.y)
                left_points.add(new_point)
            else:
                raise ValueError(f"point on a fold line: {point}")

        self.points = left_points

    def fold_left(self, position: int) -> None:
        left_points = set()

        for point in self.points:
            if point.x < position:
                left_points.add(point)
            elif point.x > position:
                new_point = Point(2 * position - point.x, point.y)
                left_points.add(new_point)
            else:
                raise ValueError(f"point on a fold line: {point}")

        self.points = left_points


class Instruction(NamedTuple):
    fold: Fold
    position: int

    @classmethod
    def from_line(cls, line: str) -> Instruction:
        raw_fold, raw_line = line.split("=")
        return Instruction(
            fold=Fold(raw_fold[-1]),
            position=int(raw_line)
        )


def parse_task(task: str) -> tuple[Paper, list[Instruction]]:
    raw_paper, raw_instructions = task.split("\n\n")

    paper = Paper.from_text(raw_paper)
    instructions = [
        Instruction.from_line(line) for line in raw_instructions.splitlines()
    ]

    return paper, instructions


def solve(task: str) -> int:
    paper, instructions = parse_task(task)
    paper.fold(instructions[0])
    return paper.visible_points
