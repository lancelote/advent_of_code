"""2020 - Day 2 Part 2: Password Philosophy."""
from src.year2020.day2a import Password
from src.year2020.day2a import Policy
from src.year2020.day2a import process_data


def xor(a: bool, b: bool) -> bool:
    return a != b


def is_valid(policy: Policy, password: Password) -> bool:
    first = password[policy.first - 1] == policy.char
    second = password[policy.second - 1] == policy.char
    return xor(first, second)


def solve(task: str) -> int:
    """Count invalid passwords."""
    data = process_data(task)
    return sum(is_valid(policy, password) for (policy, password) in data)
