"""2022 - Day 3 Part 2: Rucksack Reorganization."""
from src.year2022.day03a import priority
from src.year2022.day03a import process_data


def solve(task: str) -> int:
    result = 0
    rucksacks = process_data(task)

    for i in range(0, len(rucksacks), 3):
        a, b, c = rucksacks[i : i + 3]
        sticker = (set(a.items) & set(b.items) & set(c.items)).pop()
        result += priority(sticker)

    return result
