"""2018 - Day 9 Part 1: Marble Mania."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Player:
    """Player representation, where pk is an ID."""

    pk: int
    score: int = 0


@dataclass
class Marble:
    """Marble representation, stores the references to parent and child."""

    value: int = 0
    parent: Marble | None = None
    child: Marble | None = None

    def insert_new(self, marble: Marble) -> None:
        """Insert a new marble between 1 and 2 from self."""
        first = self.child
        if not first:
            raise ValueError("Marble has no child.")
        second = first.child
        if not second:
            raise ValueError("Marble has not child.")
        first.child = marble
        marble.parent = first
        marble.child = second
        second.parent = marble

    def remove_counter_clockwise(self, times: int) -> tuple[Marble, int]:
        """Remove item counter-clockwise after times rotations."""
        before = self
        for _ in range(times - 1):
            if not before.parent:
                raise ValueError("Marble has not parent.")
            before = before.parent
        if not before:
            raise ValueError("Counter-clockwise turn should be done >1 times.")
        remove = before.parent
        if not remove:
            raise ValueError("Marble has not parent.")
        after = remove.parent
        if not after:
            raise ValueError("Marble has not parent.")

        after.child = before
        before.parent = after
        return before, remove.value

    @classmethod
    def get_zero_marble(cls) -> Marble:
        """Instantiate first marble."""
        marble = cls()
        marble.parent = marble
        marble.child = marble
        return marble

    def __str__(self) -> str:
        return f"Marble({self.value})"


class Game:
    """Marble game."""

    def __init__(self, players_number: int, marbles: int) -> None:
        """Place a zero marble and instantiate a list of players."""
        self.turn = 0
        self.player = 0
        self.marbles = marbles
        self.players = [Player(pk=i) for i in range(players_number)]
        self.current_marble = Marble.get_zero_marble()

    def make_turn(self) -> None:
        """Make game turn."""
        self.turn += 1
        new_marble = Marble(self.turn)
        if new_marble.value % 23 == 0:
            self.current_player.score += new_marble.value
            new, score = self.current_marble.remove_counter_clockwise(7)
            self.current_marble = new
            self.current_player.score += score
        else:
            self.current_marble.insert_new(new_marble)
            self.current_marble = new_marble
        self.next_player()

    def next_player(self) -> None:
        """Update current player pk."""
        self.player = (self.player + 1) % len(self.players)

    @property
    def current_player(self) -> Player:
        """Get current player instance."""
        return self.players[self.player]

    @property
    def finished(self) -> bool:
        """Check if game is finished."""
        return self.turn == self.marbles

    @property
    def winner(self) -> Player:
        """Get winner player score."""
        return max(self.players, key=lambda player: player.score)


def parse_task(task: str) -> tuple[int, int]:
    """Return number of players and marbles."""
    parts = task.strip().split()
    return int(parts[0]), int(parts[6])


def solve(task: str) -> int:
    """Get the winner score."""
    players_number, marbles = parse_task(task)
    game = Game(players_number, marbles)

    while not game.finished:
        game.make_turn()

    return game.winner.score
