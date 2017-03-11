"""2016 - Day 7 Part 2: Internet Protocol Version 7.

You would also like to know which IPs support SSL (super-secret listening).

An IP supports SSL if it has an Area-Broadcast Accessor, or ABA, anywhere in
the supernet sequences (outside any square bracketed sections),
and a corresponding Byte Allocation Block, or BAB, anywhere in the hypernet
sequences. An ABA is any three-character sequence which consists of the same
character twice with a different character between them, such as xyx or aba.
A corresponding BAB is the same characters but in reversed positions: yxy and
bab, respectively.

For example:

  - aba[bab]xyz supports SSL (aba outside square brackets with corresponding
    bab within square brackets).
  - xyx[xyx]xyx does not support SSL (xyx, but no corresponding yxy).
  - aaa[kek]eke supports SSL (eke in supernet with corresponding kek in
    hypernet; the aaa sequence is not related, because the interior character
    must be different).
  - zazbz[bzb]cdb supports SSL (zaz has no corresponding aza, but zbz has
    a corresponding bzb, even though zaz and zbz overlap).

How many IPs in your puzzle input support SSL?
"""

from src.year2016.day7a import process_date


def solve(task: str) -> int:
    """Compute how many IPs support TLS."""
    count = 0
    ips = process_date(task)
    for ip in ips:
        if ip.support_ssl:
            count += 1
    return count
