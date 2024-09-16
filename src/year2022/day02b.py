"""2022 - Day 2 Part 2: Rock Paper Scissors."""

from src.year2022.day02a import Pick
from src.year2022.day02a import process_data


def solve(task: str) -> int:
    score = 0

    for turn in process_data(task):
        # need to lose
        if turn.your_pick is Pick.ROCK:
            if turn.other_pick is Pick.ROCK:
                score += Pick.SCISSORS.value
            elif turn.other_pick is Pick.PAPER:
                score += Pick.ROCK.value
            else:
                score += Pick.PAPER.value

        # need a draw
        elif turn.your_pick is Pick.PAPER:
            score += turn.other_pick.value
            score += 3

        # need to win
        else:
            if turn.other_pick is Pick.ROCK:
                score += Pick.PAPER.value
            elif turn.other_pick is Pick.PAPER:
                score += Pick.SCISSORS.value
            else:
                score += Pick.ROCK.value
            score += 6

    return score
