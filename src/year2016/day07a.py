"""2016 - Day 7 Part 1: Internet Protocol Version 7."""

from collections.abc import Generator


class IP:
    """IPv7 representation."""

    def __init__(
        self, supernet_parts: list[str], hypernet_parts: list[str]
    ) -> None:
        """Create an IPv7 instance.

        Args:
            supernet_parts: parts outside of square brackets
            hypernet_parts: parts inside square brackets

        """
        self.supernet_parts = supernet_parts
        self.hypernet_parts = hypernet_parts

    @staticmethod
    def _has_abba(part: str) -> bool:
        """Check if the string has ABBA."""
        for i in range(max(len(part) - 3, 0)):
            if (
                part[i] == part[i + 3]
                and part[i + 1] == part[i + 2]
                and part[i] != part[i + 1]
            ):
                return True
        return False

    @property
    def support_tls(self) -> bool:
        """Check if the IP supports TLS."""
        for part in self.hypernet_parts:
            if self._has_abba(part):
                return False
        for part in self.supernet_parts:
            if self._has_abba(part):
                return True
        return False

    @property
    def abas(self) -> Generator[str]:
        """Generate abas from supernet parts."""
        for super_part in self.supernet_parts:
            for i in range(max(len(super_part) - 2, 0)):
                if super_part[i] == super_part[i + 2] != super_part[i + 1]:
                    yield super_part[i : i + 3]

    @property
    def support_ssl(self) -> bool:
        """Check if the IP supports SSL."""
        for aba in self.abas:
            for hyper_part in self.hypernet_parts:
                bab = aba[1] + aba[0] + aba[1]
                if bab in hyper_part:
                    return True
        return False

    def __eq__(self, other: object) -> bool:
        """Check for IP equality by comparing supernet and hypernet parts."""
        if not isinstance(other, IP):
            return False
        return (
            self.supernet_parts == other.supernet_parts
            and self.hypernet_parts == other.hypernet_parts
        )


def process_line(line: str) -> IP:
    """Find all supernet and hypernet parts inside one line (ip)."""
    part = ""
    supernet_parts = []
    hypernet_parts = []

    for char in line:
        if char == "[":
            supernet_parts.append(part)
            part = ""
        elif char == "]":
            hypernet_parts.append(part)
            part = ""
        else:
            part += char

    if part:
        supernet_parts.append(part)
    return IP(supernet_parts, hypernet_parts)


def process_date(data: str) -> list[IP]:
    """Convert raw data in the list of ips with supernet and hypernet parts."""
    ips = []
    for line in data.strip().split("\n"):
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
