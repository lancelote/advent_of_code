"""2024 - Day 15 Part 1: Warehouse Woes"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from dataclasses import dataclass
from enum import StrEnum


class Instruction(StrEnum):
    NORTH = "^"
    EAST = ">"
    SOUTH = "v"
    WEST = "<"


SHIFTS = {
    # dr, dc
    Instruction.NORTH: (-1, 0),
    Instruction.EAST: (0, +1),
    Instruction.SOUTH: (+1, 0),
    Instruction.WEST: (0, -1),
}


@dataclass
class Object(ABC):
    r: int
    c: int
    symbol: str

    @abstractmethod
    def move(self, instruction: Instruction, warehouse: Warehouse) -> bool:
        raise NotImplementedError


class Moveable(Object, ABC):
    def move(self, instruction: Instruction, warehouse: Warehouse) -> bool:
        dr, dc = SHIFTS[instruction]
        nr, nc = self.r + dr, self.c + dc

        if (nr, nc) in warehouse.objects:
            neighbor = warehouse.objects[(nr, nc)]
            if neighbor.move(instruction, warehouse):
                self.update_position(nr, nc, warehouse)
                return True
            else:
                return False
        else:
            self.update_position(nr, nc, warehouse)
            return True

    def update_position(self, nr: int, nc: int, warehouse: Warehouse) -> None:
        del warehouse.objects[(self.r, self.c)]
        self.r, self.c = nr, nc
        warehouse.objects[(nr, nc)] = self


class Wall(Object):
    def move(self, instruction: Instruction, warehouse: Warehouse) -> bool:
        return False


class Box(Moveable):
    @property
    def gps(self) -> int:
        return self.r * 100 + self.c


class Robot(Moveable): ...


@dataclass
class Warehouse:
    height: int
    width: int
    robot: Robot
    objects: dict[tuple[int, int], Object]
    boxes: list[Box]

    @classmethod
    def from_text(cls, text: str) -> Warehouse:
        robot = Robot(r=0, c=0, symbol="@")
        objects: dict[tuple[int, int], Object] = {}
        boxes: list[Box] = []

        lines = text.split("\n")
        height, width = len(lines), len(lines[0])

        for r, row in enumerate(lines):
            for c, x in enumerate(row):
                if x == "#":
                    objects[(r, c)] = Wall(r, c, symbol="#")
                elif x == "@":
                    robot.r, robot.c = r, c
                    objects[(r, c)] = robot
                elif x == "O":
                    box = Box(r, c, symbol="O")
                    boxes.append(box)
                    objects[(r, c)] = box

        return cls(height, width, robot, objects, boxes)

    def move_robot(self, instructions: list[Instruction]) -> None:
        for instruction in instructions:
            self.robot.move(instruction, self)

    @property
    def gps_sum(self) -> int:
        return sum(box.gps for box in self.boxes)

    def __str__(self) -> str:
        lines = [["."] * self.width for _ in range(self.height)]

        for (r, c), v in self.objects.items():
            lines[r][c] = v.symbol

        return "\n".join("".join(line) for line in lines)


def process_data(task: str) -> tuple[Warehouse, list[Instruction]]:
    first, second = task.split("\n\n")
    warehouse = Warehouse.from_text(first)
    instructions = [Instruction(x) for x in second if x in Instruction]
    return warehouse, instructions


def solve(task: str) -> int:
    warehouse, instructions = process_data(task)
    warehouse.move_robot(instructions)
    return warehouse.gps_sum
