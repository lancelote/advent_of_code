"""2025 - Day 3 Part 1: Lobby"""


def process_data(task: str) -> list[list[int]]:
    return [[int(x) for x in line] for line in task.splitlines()]


def max_joltage(bank: list[int]) -> int:
    li = 0

    left = bank[li]
    right = bank[len(bank) - 1]

    for i in range(len(bank) - 1):
        if left == 9:
            break

        if bank[i] > left:
            li = i
            left = bank[i]

    for j in range(len(bank) - 1, li, -1):
        if right == 9:
            break

        if bank[j] > right:
            right = bank[j]

    return left * 10 + right


def solve(task: str) -> int:
    banks = process_data(task)
    return sum(max_joltage(bank) for bank in banks)
