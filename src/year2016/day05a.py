"""2016 - Day 5 Part 1: How About a Nice Game of Chess.

You are faced with a security door designed by Easter Bunny engineers that seem
to have acquired most of their security knowledge by watching hacking movies.

The eight-character password for the door is generated one character at a time
by finding the MD5 hash of some Door ID (your puzzle input) and an increasing
integer index (starting with 0).

A hash indicates the next character in the password if its hexadecimal
representation starts with five zeroes. If it does, the sixth character in the
hash is the next character of the password.

For example, if the Door ID is abc:

  - The first index which produces a hash that starts with five zeroes is
    3231929, which we find by hashing abc3231929; the sixth character of the
    hash, and thus the first character of the password, is 1.
  - 5017308 produces the next interesting hash, which starts with 000008f82...,
    so the second character of the password is 8.
  - The third time a hash starts with five zeroes is for abc5278568,
    discovering the character f.

In this example, after continuing this search a total of eight times,
the password is 18f47a30.

Given the actual Door ID, what is the password?
"""
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
