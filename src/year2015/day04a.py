"""2015 - Day 4 Part 1: The Ideal Stocking Stuffer."""

from hashlib import md5


def get_md5_cache(num: int, key: str) -> str:
    message = key + str(num)
    return md5(message.encode()).hexdigest()


def solve(task: str, zeros: int = 5) -> int:
    num = 0
    while not get_md5_cache(num, task).startswith("0" * zeros):
        num += 1
    return num
