"""2019 - Day 13 Part 2: Care Package."""
import os
from enum import Enum

from src.year2019.intcode import Computer


class Tile(Enum):
    """Arcade screen tile."""

    EMPTY = 0
    WALL = 1
    BLOCK = 2
    PADDLE = 3
    BALL = 4

    def __str__(self) -> str:
        if self.value == 0:
            return " "
        elif self.value == 1:
            return "#"
        elif self.value == 2:
            return "□"
        elif self.value == 3:
            return "-"
        elif self.value == 4:
            return "o"
        else:
            raise ValueError(f"unknown enum value: {self.value}")


class Arcade:
    """Arcade game."""

    def __init__(self, program: str, cpu: Computer | None = None):
        """Program is a puzzle input and cpu - IntCode computer."""
        self.cpu = cpu or Computer()
        self.cpu.load_program(program)
        self.ball_x = 0
        self.paddle_x = 0
        self.map: dict[tuple[int, int], Tile] = dict()
        self.score = 0

    def play(self) -> None:
        """Play game until win or lose."""
        self.make_free()

        while not self.is_finished:
            self.cpu.execute()
            self.update_map()
            self.print()
            self.move_paddle()
            os.system("clear")

    def move_paddle(self) -> None:
        """Move paddle automatically depending on ball position."""
        if self.ball_x > self.paddle_x:
            move = 1
        elif self.ball_x < self.paddle_x:
            move = -1
        else:
            move = 0
        self.cpu.stdin.append(move)

    def update_map(self) -> None:
        """Update tile - coordinates map after a game step."""
        while self.cpu.stdout:
            x = self.cpu.stdout.popleft()
            y = self.cpu.stdout.popleft()
            pk = self.cpu.stdout.popleft()

            if x == -1 and y == 0:
                self.score = pk
            else:
                if pk == 3:
                    self.paddle_x = x
                if pk == 4:
                    self.ball_x = x
                self.map[(x, y)] = Tile(pk)

    def print(self) -> None:
        """Print the game screen."""
        max_x = max(self.map.keys(), key=lambda point: point[0])[0]
        max_y = max(self.map.keys(), key=lambda point: point[1])[1]

        canvas: list[list[Tile]] = [
            [Tile.EMPTY for _ in range(max_x + 1)] for _ in range(max_y + 1)
        ]

        for (x, y), tile in self.map.items():
            canvas[y][x] = tile

        for row in canvas:
            for item in row:
                print(item, end="")
            print()

    def make_free(self) -> None:
        """Allow playing free."""
        self.cpu.load_sram_to_dram()
        self.cpu[0] = 2

    @property
    def is_finished(self) -> bool:
        """Check if the game is finished."""
        return self.cpu.is_halt


def solve(task: str) -> int:
    """Win the game and get the final score."""
    arcade = Arcade(task)
    arcade.play()
    return arcade.score
