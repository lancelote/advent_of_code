"""2024 - Day 15 Part 2: Warehouse Woes"""

from __future__ import annotations

from abc import ABC, abstractmethod
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
    symbol: str
    r: int
    c: int

    @abstractmethod
    def can_move(self, instruction: Instruction, warehouse: Warehouse) -> bool:
        raise NotImplementedError

    @abstractmethod
    def move(self, instruction: Instruction, warehouse: Warehouse) -> None:
        raise NotImplementedError

    @abstractmethod
    def update_position(self, nr: int, nc: int, warehouse: Warehouse) -> None:
        raise NotImplementedError


class Bulky(Object, ABC):
    def can_move(self, instruction: Instruction, warehouse: Warehouse) -> bool:
        moveable = True

        dr, dc = SHIFTS[instruction]
        nr, nc = self.r + dr, self.c + dc

        if (nr, nc) in warehouse.objects:
            neighbor1 = warehouse.objects[(nr, nc)]
            moveable &= neighbor1 is self or neighbor1.can_move(instruction, warehouse)
        if (nr, nc + 1) in warehouse.objects:
            neighbor2 = warehouse.objects[(nr, nc + 1)]
            moveable &= neighbor2 is self or neighbor2.can_move(instruction, warehouse)

        return moveable

    def move(self, instruction: Instruction, warehouse: Warehouse) -> None:
        if self.can_move(instruction, warehouse):
            dr, dc = SHIFTS[instruction]
            nr, nc = self.r + dr, self.c + dc

            if (nr, nc) in warehouse.objects:
                neighbor = warehouse.objects[(nr, nc)]
                if neighbor is not self:
                    neighbor.move(instruction, warehouse)

            if (nr, nc + 1) in warehouse.objects:
                neighbor = warehouse.objects[(nr, nc + 1)]
                if neighbor is not self:
                    neighbor.move(instruction, warehouse)

            self.update_position(nr, nc, warehouse)

    def update_position(self, nr: int, nc: int, warehouse: Warehouse) -> None:
        del warehouse.objects[(self.r, self.c)]
        del warehouse.objects[(self.r, self.c + 1)]

        self.r, self.c = nr, nc

        warehouse.objects[(nr, nc)] = self
        warehouse.objects[(nr, nc + 1)] = self


class Wall(Bulky):
    def can_move(self, instruction: Instruction, warehouse: Warehouse) -> bool:
        return False

    def move(self, instruction: Instruction, warehouse: Warehouse) -> None: ...


class Box(Bulky):
    @property
    def gps(self) -> int:
        return self.r * 100 + self.c


class Robot(Object):
    def can_move(self, instruction: Instruction, warehouse: Warehouse) -> bool:
        dr, dc = SHIFTS[instruction]
        nr, nc = self.r + dr, self.c + dc

        if (nr, nc) in warehouse.objects:
            neighbor = warehouse.objects[(nr, nc)]
            return neighbor.can_move(instruction, warehouse)
        else:
            return True

    def move(self, instruction: Instruction, warehouse: Warehouse) -> None:
        if self.can_move(instruction, warehouse):
            dr, dc = SHIFTS[instruction]
            nr, nc = self.r + dr, self.c + dc
            if (nr, nc) in warehouse.objects:
                neighbor = warehouse.objects[(nr, nc)]
                neighbor.move(instruction, warehouse)
            self.update_position(nr, nc, warehouse)

    def update_position(self, nr: int, nc: int, warehouse: Warehouse) -> None:
        del warehouse.objects[(self.r, self.c)]
        self.r, self.c = nr, nc
        warehouse.objects[(nr, nc)] = self


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
        height, width = len(lines), len(lines[0] * 2)

        for r, row in enumerate(lines):
            for c, x in enumerate(row):
                if x == "#":
                    wall = Wall("#", r, c * 2)
                    objects[(r, c * 2)] = wall
                    objects[(r, c * 2 + 1)] = wall
                elif x == "@":
                    robot.r, robot.c = r, c * 2
                    objects[(r, c * 2)] = robot
                elif x == "O":
                    box = Box("O", r, c * 2)
                    boxes.append(box)
                    objects[(r, c * 2)] = box
                    objects[(r, c * 2 + 1)] = box

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
