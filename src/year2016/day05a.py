"""2016 - Day 5 Part 1: How About a Nice Game of Chess."""

import hashlib


def solve(task: str) -> str:
    """Find the secret door password."""
    i = 0
    password = ""

    while len(password) != 8:
        next_try = task + str(i)
        hex_hash = hashlib.md5(next_try.encode("utf-8")).hexdigest()
        if hex_hash.startswith("00000"):
            password += hex_hash[5]
        i += 1
    return password
