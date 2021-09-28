"""2020 - Day 15 Part 2: Rambunctious Recitation."""
from src.year2020.day15a import play
from src.year2020.day15a import process_data


def solve(task: str) -> int:
    starting_nums = process_data(task)
    last_num = play(starting_nums, 30000000)
    return last_num
