"""2023 - Day 4 Part 2: Scratchcards"""

from collections import defaultdict

from src.year2023.day04a import process_data


def solve(task: str) -> int:
    count = 0
    cards = process_data(task)
    copies: dict[int, int] = defaultdict(lambda: 1)

    for i, card in enumerate(cards):
        count += copies[i]
        for j in range(1, card.matching + 1):
            if i + j < len(cards):
                copies[i + j] += copies[i]

    return count
