# pylint: disable=too-few-public-methods

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

from typing import List


class IP(object):
    """IPv7 representation."""

    def __init__(self,
                 main_parts: List[str],
                 hypernet_parts: List[str]) -> None:
        """Create an IPv7 instance.

        Args:
            main_parts: parts outside of square brackets
            hypernet_parts: parts inside square brackets
        """
        self.main_parts = main_parts
        self.hypernet_parts = hypernet_parts

    @staticmethod
    def _has_abba(part: str) -> bool:
        """Check if the string has ABBA."""
        for i in range(max(len(part) - 3, 0)):
            if part[i] == part[i + 3] \
                    and part[i + 1] == part[i + 2] \
                    and part[i] != part[i + 1]:
                return True
        return False

    @property
    def support_tls(self) -> bool:
        """Check if the ip supports TLS."""
        for part in self.hypernet_parts:
            if self._has_abba(part):
                return False
        for part in self.main_parts:
            if self._has_abba(part):
                return True

    def __eq__(self, other: object) -> bool:
        """Check for IP equality by comparing main and hypernet parts."""
        if not isinstance(other, IP):
            return False
        return self.main_parts == other.main_parts and \
            self.hypernet_parts == other.hypernet_parts


def process_line(line: str) -> IP:
    """Find all main and hypernet parts inside one line (ip)."""
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
    """Convert raw data in the list of ips with main and hypernet parts."""
    ips = []
    for line in data.strip().split('\n'):
        ips.append(process_line(line))
    return ips


def solve(task: str) -> int:
    """Compute gow many IPs support TLS."""
    count = 0
    ips = process_date(task)
    for ip in ips:
        if ip.support_tls:
            count += 1
    return count
