"""2018 - Day 9 Part 1: Marble Mania.

You talk to the Elves while you wait for your navigation system to initialize.
To pass the time, they introduce you to their favorite marble game.

The Elves play this game by taking turns arranging the marbles in a circle
according to very particular rules. The marbles are numbered starting with 0
and increasing by 1 until every marble has a number.

First, the marble numbered 0 is placed in the circle. At this point, while it
contains only a single marble, it is still a circle: the marble is both
clockwise from itself and counter-clockwise from itself. This marble is
designated the current marble.

Then, each Elf takes a turn placing the lowest-numbered remaining marble into
the circle between the marbles that are 1 and 2 marbles clockwise of the
current marble. (When the circle is large enough, this means that there is one
marble between the marble that was just placed and the current marble.) The
marble that was just placed then becomes the current marble.

However, if the marble that is about to be placed has a number which is a
multiple of 23, something entirely different happens. First, the current player
keeps the marble they would have placed, adding it to their score. In addition,
the marble 7 marbles counter-clockwise from the current marble is removed from
the circle and also added to the current player's score. The marble located
immediately clockwise of the marble that was removed becomes the new current
marble.

For example, suppose there are 9 players. After the marble with value 0 is
placed in the middle, each player (shown in square brackets) takes a turn. The
result of each of those turns would produce circles of marbles like this, where
clockwise is to the right and the resulting current marble is in parentheses:

00 [-] (0)
01 [1]  0 (1)
02 [2]  0 (2) 1
03 [3]  0  2  1 (3)
04 [4]  0 (4) 2  1  3
05 [5]  0  4  2 (5) 1  3
06 [6]  0  4  2  5  1 (6) 3
07 [7]  0  4  2  5  1  6  3 (7)
08 [8]  0 (8) 4  2  5  1  6  3  7
09 [9]  0  8  4 (9) 2  5  1  6  3  7
10 [1]  0  8  4  9  2(10) 5  1  6  3  7
11 [2]  0  8  4  9  2 10  5(11) 1  6  3  7
12 [3]  0  8  4  9  2 10  5 11  1(12) 6  3  7
13 [4]  0  8  4  9  2 10  5 11  1 12  6(13) 3  7
14 [5]  0  8  4  9  2 10  5 11  1 12  6 13  3(14) 7
15 [6]  0  8  4  9  2 10  5 11  1 12  6 13  3 14  7(15)
16 [7]  0(16) 8  4  9  2 10  5 11  1 12  6 13  3 14  7 15
17 [8]  0 16  8(17) 4  9  2 10  5 11  1 12  6 13  3 14  7 15
18 [9]  0 16  8 17  4(18) 9  2 10  5 11  1 12  6 13  3 14  7 15
19 [1]  0 16  8 17  4 18  9(19) 2 10  5 11  1 12  6 13  3 14  7 15
20 [2]  0 16  8 17  4 18  9 19  2(20)10  5 11  1 12  6 13  3 14  7 15
21 [3]  0 16  8 17  4 18  9 19  2 20 10(21) 5 11  1 12  6 13  3 14  7 15
22 [4]  0 16  8 17  4 18  9 19  2 20 10 21  5(22)11  1 12  6 13  3 14  7 15
23 [5]  0 16  8 17  4 18(19) 2 20 10 21  5 22 11  1 12  6 13  3 14  7 15
24 [6]  0 16  8 17  4 18 19  2(24)20 10 21  5 22 11  1 12  6 13  3 14  7 15
25 [7]  0 16  8 17  4 18 19  2 24 20(25)10 21  5 22 11  1 12  6 13  3 14  7 15

The goal is to be the player with the highest score after the last marble is
used up. Assuming the example above ends after the marble numbered 25, the
winning score is 23+9=32 (because player 5 kept marble 23 and removed marble 9,
while no other player got any points in this very short example game).

Here are a few more examples:

    10 players; last marble is worth 1618 points: high score is 8317
    13 players; last marble is worth 7999 points: high score is 146373
    17 players; last marble is worth 1104 points: high score is 2764
    21 players; last marble is worth 6111 points: high score is 54718
    30 players; last marble is worth 5807 points: high score is 37305

What is the winning Elf's score?
"""

from typing import Optional, Tuple
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
    parent: Optional['Marble'] = None
    child: Optional['Marble'] = None

    def insert_new(self, marble: 'Marble'):
        """Insert a new marble between 1 and 2 from self."""
        first = self.child
        if not first:
            raise ValueError('Marble has no child.')
        second = first.child
        if not second:
            raise ValueError('Marble has not child.')
        first.child = marble
        marble.parent = first
        marble.child = second
        second.parent = marble

    def remove_counter_clockwise(self, times: int) -> Tuple['Marble', int]:
        """Remove item counter clockwise after times rotations."""
        before = self
        for _ in range(times - 1):
            if not before.parent:
                raise ValueError('Marble has not parent.')
            before = before.parent
        if not before:
            raise ValueError('Counter clockwise turn should be done >1 times.')
        remove = before.parent
        if not remove:
            raise ValueError('Marble has not parent.')
        after = remove.parent
        if not after:
            raise ValueError('Marble has not parent.')

        after.child = before
        before.parent = after
        return before, remove.value

    @classmethod
    def get_zero_marble(cls) -> 'Marble':
        """Instantiate first marble."""
        marble = cls()
        marble.parent = marble
        marble.child = marble
        return marble

    def __str__(self):
        return f'Marble({self.value})'


class Game:
    """Marble game."""

    def __init__(self, players_number: int, marbles: int):
        """Place a zero marble and instantiate a list of players."""
        self.turn = 0
        self.player = 0
        self.marbles = marbles
        self.players = [Player(pk=i) for i in range(players_number)]
        self.current_marble = Marble.get_zero_marble()

    def make_turn(self):
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

    def next_player(self):
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


def parse_task(task: str) -> Tuple[int, int]:
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
