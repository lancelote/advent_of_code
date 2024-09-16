"""2022 - Day 2 Part 1: Rock Paper Scissors."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class Pick(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    @classmethod
    def from_char(cls, char: str) -> Pick:
        if char == "A":
            return Pick.ROCK
        elif char == "B":
            return Pick.PAPER
        elif char == "C":
            return Pick.SCISSORS
        elif char == "X":
            return Pick.ROCK
        elif char == "Y":
            return Pick.PAPER
        elif char == "Z":
            return Pick.SCISSORS
        else:
            raise ValueError(f"unknown other pick char: {char}")


@dataclass
class Turn:
    other_pick: Pick
    your_pick: Pick

    @classmethod
    def from_line(cls, line: str) -> Turn:
        other_char, your_char = line.split(" ")
        other_pick = Pick.from_char(other_char)
        your_pick = Pick.from_char(your_char)
        return Turn(other_pick, your_pick)


def process_data(task: str) -> list[Turn]:
    return [Turn.from_line(line) for line in task.strip().split("\n")]


def solve(task: str) -> int:
    score = 0

    for turn in process_data(task):
        score += turn.your_pick.value

        if turn.other_pick is turn.your_pick:
            score += 3
        elif turn.your_pick is Pick.ROCK and turn.other_pick is Pick.SCISSORS:
            score += 6
        elif turn.your_pick is Pick.PAPER and turn.other_pick is Pick.ROCK:
            score += 6
        elif turn.your_pick is Pick.SCISSORS and turn.other_pick is Pick.PAPER:
            score += 6

    return score
