"""2023 - Day 2 Part 1: Cube Conundrum"""

from dataclasses import dataclass
from typing import Self


@dataclass
class Round:
    red: int
    green: int
    blue: int

    @classmethod
    def from_string(cls, s: str) -> Self:
        # e.g., "12 blue, 15 red, 2 green"
        color_parts = s.split(", ")

        red = 0
        green = 0
        blue = 0

        for color_part in color_parts:
            num_str, color = color_part.split(" ")

            if color == "red":
                red = int(num_str)
            elif color == "green":
                green = int(num_str)
            elif color == "blue":
                blue = int(num_str)
            else:
                raise ValueError(f"unknown color {color}")

        return cls(red, green, blue)


@dataclass
class Game:
    pk: int
    rounds: list[Round]

    @classmethod
    def from_line(cls, line: str) -> Self:
        # e.g., "Game 1: 12 blue, 15 red, 2 green; 17 red, 8 green, 5 blue;"

        game_part, rounds_part = line.split(": ")

        # game primary key
        _, pk_str = game_part.split(" ")
        pk = int(pk_str)

        round_strs = rounds_part.split("; ")
        rounds = [Round.from_string(r_str) for r_str in round_strs]

        return cls(pk, rounds)


def process_data(task: str) -> list[Game]:
    return [Game.from_line(line) for line in task.splitlines()]


def solve(task: str) -> int:
    count = 0
    games = process_data(task)

    for game in games:
        for r in game.rounds:
            if r.red > 12 or r.green > 13 or r.blue > 14:
                break
        else:
            count += game.pk

    return count
