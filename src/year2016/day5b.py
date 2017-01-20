"""2016 - Day 5 Part 2: How About a Nice Game of Chess.

As the door slides open, you are presented with a second door that uses a
slightly more inspired security mechanism. Clearly unimpressed by the last
version (in what movie is the password decrypted in order?!), the Easter Bunny
engineers have worked out a better solution.

Instead of simply filling in the password from left to right, the hash now also
indicates the position within the password to fill. You still look for hashes
that begin with five zeroes; however, now, the sixth character represents the
position (0-7), and the seventh character is the character to put in that
position.

A hash result of 000001f means that f is the second character in the password.
Use only the first result for each position, and ignore invalid positions.

For example, if the Door ID is abc:

  - The first interesting hash is from abc3231929, which produces 0000015...;
    so, 5 goes in position 1: _5______.
  - In the previous method, 5017308 produced an interesting hash; however,
    it is ignored, because it specifies an invalid position (8).
  - The second interesting hash is at index 5357525, which produces 000004e...;
    so, e goes in position 4: _5__e___.

You almost choke on your popcorn as the final character falls into place,
producing the password 05ace8e3.

Given the actual Door ID and this new method, what is the password? Be extra
proud of your solution if it uses a cinematic "decrypting" animation.
"""

import hashlib
from typing import List  # noqa


def print_password(password):
    """Print current password decipher progress."""
    line = ' '.join(char if char is not None else 'x' for char in password)
    print('Hacking... ', line, end='\r')


def solve(task: str) -> str:
    """Find the secret door password."""
    i = 0
    password = [None] * 8  # type: List[str]
    print_password(password)

    while None in password:
        next_try = task + str(i)
        hex_hash = hashlib.md5(next_try.encode('utf-8')).hexdigest()
        position_char = hex_hash[5]
        new_char = hex_hash[6]

        try:
            position = int(position_char)

            if hex_hash.startswith('00000') and password[position] is None:
                password[position] = new_char
                print_password(password)
        except (ValueError, IndexError):
            pass
        i += 1
    print()
    return ''.join(password)