"""2018 - Day 9 Part 2: Marble Mania.

Amused by the speed of your answer, the Elves are curious:

What would the new winning Elf's score be if the number of the last marble were
100 times larger?
"""
from src.year2018.day9a import Game
from src.year2018.day9a import parse_task


def solve(task: str) -> int:
    """Get the winner score if the last marble is 100 times larger."""
    players_number, marbles = parse_task(task)
    game = Game(players_number, marbles * 100)

    while not game.finished:
        game.make_turn()

    return game.winner.score
