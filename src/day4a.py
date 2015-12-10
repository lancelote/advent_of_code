# coding=utf-8

"""
--- Day 4: The Ideal Stocking Stuffer ---

Santa needs help mining some AdventCoins (very similar to bitcoins) to use as
gifts for all the economically forward-thinking little girls and boys.

To do this, he needs to find MD5 hashes which, in hexadecimal, start with at
least five zeroes. The input to the MD5 hash is some secret key (your puzzle
input, given below) followed by a number in decimal. To mine AdventCoins, you
must find Santa the lowest positive number (no leading zeroes: 1, 2, 3, ...)
that produces such a hash.

For example:

    If your secret key is abcdef, the answer is 609043, because the MD5 hash
    of abcdef609043 starts with five zeroes (000001dbbfa...), and it is the
    lowest such number to do so.

    If your secret key is pqrstuv, the lowest number it combines with to make
    an MD5 hash starting with five zeroes is 1048970; that is, the MD5 hash
    of pqrstuv1048970 looks like 000006136ef....
"""

from hashlib import md5


def solve(task, zeros=5):
    """
    Solve the puzzle

    Args:
        zeros (int): number of zeros to find
        task (str): key to encode

    Returns:
        int: Biggest number
    """
    i = 0
    message_hash = ''
    while not message_hash.startswith('0'*zeros):
        message = task + str(i)
        message_hash = md5(message.encode()).hexdigest()
        i += 1
    return i - 1
