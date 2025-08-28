"""2018 - Day 9 Part 2: Marble Mania."""

from src.year2018.day09a import Game, parse_task


def solve(task: str) -> int:
    """Get the winner score if the last marble is 100 times larger."""
    players_number, marbles = parse_task(task)
    game = Game(players_number, marbles * 100)

    while not game.finished:
        game.make_turn()

    return game.winner.score
