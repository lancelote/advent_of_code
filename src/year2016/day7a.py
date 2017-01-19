"""Day 7: Internet Protocol Version 7.

While snooping around the local network of EBHQ, you compile a list of IP
addresses (they're IPv7, of course; IPv6 is much too limited). You'd like
to figure out which IPs support TLS (transport-layer snooping).

An IP supports TLS if it has an Autonomous Bridge Bypass Annotation, or ABBA.
An ABBA is any four-character sequence which consists of a pair of two
different characters followed by the reverse of that pair, such as xyyx or
abba. However, the IP also must not have an ABBA within any hypernet sequences,
which are contained by square brackets.

For example:

  - abba[mnop]qrst supports TLS (abba outside square brackets).
  - abcd[bddb]xyyx does not support TLS (bddb is within square brackets,
    even though xyyx is outside square brackets).
  - aaaa[qwer]tyui does not support TLS (aaaa is invalid; the interior
    characters must be different).
  - ioxxoj[asdfgh]zxcvbn supports TLS (oxxo is outside square brackets,
    even though it's within a larger string).

How many IPs in your puzzle input support TLS?
"""

from collections import namedtuple
from typing import List, Tuple

IP = namedtuple('IP', 'main_parts hypernet_parts')


def process_line(line: str) -> IP:
    """Find all main and hypernet parts inside one line (ip)"""
    # ToDo: Bad input checks
    part = ''
    main_parts = []
    hypernet_parts = []

    for char in line:
        if char == '[':
            main_parts.append(part)
            part = ''
        elif char == ']':
            hypernet_parts.append(part)
            part = ''
        else:
            part += char

    if part:
        main_parts.append(part)
    return IP(main_parts, hypernet_parts)


def process_date(data: str) -> List[IP]:
    """Convert raw data in the list of ips with main and hypernet parts"""
    ips = []
    for line in data.strip().split('\n'):
        ips.append(process_line(line))
    return ips


def support_tls(ip: IP) -> bool:
    """Check if the ip supports TLS"""
    raise NotImplementedError


def solve(task: str) -> int:
    """Compute gow many IPs support TLS"""
    count = 0
    ips = process_date(task)
    for ip in ips:
        if support_tls(ip):
            count += 1
    return count
