"""
The game didn't run because you didn't put in any quarters. Unfortunately, you
did not bring any quarters. Memory address 0 represents the number of quarters
that have been inserted; set it to 2 to play for free.

The arcade cabinet has a joystick that can move left and right. The software
reads the position of the joystick with input instructions:

    If the joystick is in the neutral position, provide 0.
    If the joystick is tilted to the left, provide -1.
    If the joystick is tilted to the right, provide 1.

The arcade cabinet also has a segment display capable of showing a single
number that represents the player's current score. When three output
instructions specify X=-1, Y=0, the third output instruction is not a tile;
the value instead specifies the new score to show in the segment display.
For example, a sequence of output values like -1,0,12345 would show 12345 as
the player's current score.

Beat the game by breaking all the blocks. What is your score after the last
block is broken?
"""

from dataclasses import dataclass
from enum import Enum
from typing import Dict, List

from src.year2019.intcode import Computer


class Tile(Enum):
    EMPTY = 0
    WALL = 1
    BLOCK = 2
    PADDLE = 3
    BALL = 4

    def __str__(self):
        if self.value == 0:
            return ' '
        elif self.value == 1:
            return '#'
        elif self.value == 2:
            return '□'
        elif self.value == 3:
            return '-'
        elif self.value == 4:
            return 'o'


@dataclass
class Ball:
    x: int = 0
    y: int = 0
    dx: int = 0


@dataclass
class Paddle:
    x: int = 0


class Arcade:
    def __init__(self, program: str, cpu: Computer = None):
        self.cpu = cpu or Computer()
        self.cpu.load_program(program)
        self.ball = Ball()
        self.paddle = Paddle()
        self.map: Dict[(int, int): Tile] = dict()
        self.score = 0

    def play(self):
        self.make_free()

        while not self.is_finished:
            self.cpu.execute()
            self.cpu.stdin.append(0)
            self.update_map()
            self.print()
            input()

    def update_map(self):
        while self.cpu.stdout:
            x = self.cpu.stdout.popleft()
            y = self.cpu.stdout.popleft()
            pk = self.cpu.stdout.popleft()

            if x == -1 and y == 0:
                self.score = pk
            else:
                self.map[(x, y)] = Tile(pk)

    def print(self):
        max_x = max(self.map.keys(), key=lambda point: point[0])[0]
        max_y = max(self.map.keys(), key=lambda point: point[1])[1]

        canvas: List[List[Tile]] = [
            [Tile.EMPTY for _ in range(max_x + 1)]
            for _ in range(max_y + 1)
        ]

        for ((x, y), tile) in self.map.items():
            canvas[y][x] = tile

        for row in canvas:
            for item in row:
                print(item, end='')
            print()

    def make_free(self):
        self.cpu.load_sram_to_dram()
        self.cpu[0] = 2

    @property
    def is_finished(self) -> bool:
        return self.cpu.is_halt


def solve(task: str) -> int:
    arcade = Arcade(task)
    arcade.play()
    return arcade.score
