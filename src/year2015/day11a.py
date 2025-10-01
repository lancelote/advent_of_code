"""2015 - Day 11 Part 1: Corporate Policy."""

from string import ascii_lowercase

TO_INT = {x: i for i, x in enumerate(ascii_lowercase)}
TO_STR = dict(enumerate(ascii_lowercase))
BANNED = {8, 11, 14}


def to_num(line: str) -> list[int]:
    return [TO_INT[x] for x in line][::-1]


def to_str(num: list[int]) -> str:
    return "".join(TO_STR[x] for x in num)[::-1]


def incr(num: list[int]) -> None:
    i = 0
    left = 1

    while left and i < len(num):
        num[i] = (num[i] + left) % 26
        left = num[i] == 0
        i += 1

    if left:
        num.append(1)


def has_banned(num: list[int]) -> bool:
    for x in num:
        if x in BANNED:
            return True
    return False


def has_two_pairs(num: list[int]) -> bool:
    pairs = 0
    used_pair_digits: set[int] = set()

    i = 0
    while i < len(num) - 1:
        if num[i] == num[i + 1] and num[i] not in used_pair_digits:
            pairs += 1
            used_pair_digits.add(num[i])
            i += 1
        if pairs == 2:
            return True
        i += 1
    return False


def has_straight(num: list[int]) -> bool:
    for i in range(len(num) - 2):
        if num[i] == (num[i + 1] + 1) % 26 == (num[i + 2] + 2) % 26:
            return True
    return False


def is_valid(num: list[int]) -> bool:
    return not has_banned(num) and has_two_pairs(num) and has_straight(num)


def solve(task: str) -> str:
    num = to_num(task)

    while not is_valid(num):
        incr(num)

    return to_str(num)
