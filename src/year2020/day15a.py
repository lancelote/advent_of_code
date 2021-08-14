"""2020 - Day 15 Part 1: Rambunctious Recitation."""


def process_data(task: str) -> list[int]:
    return [int(x) for x in task.split(",")]


def play(starting_nums: list[int], times=2020) -> int:
    num = 0
    last_diff = 0
    turn = 1
    turns: dict[int, int] = {}

    for num in starting_nums:
        last_diff = turn - turns.get(num, turn)
        turns[num] = turn
        turn += 1
        times -= 1

    while times:
        num = last_diff
        last_diff = turn - turns.get(num, turn)
        turns[num] = turn
        turn += 1
        times -= 1

    return num


def solve(task: str) -> int:
    starting_nums = process_data(task)
    last_num = play(starting_nums)
    return last_num
