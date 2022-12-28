"""2016 - Day 7 Part 2: Internet Protocol Version 7."""
from src.year2016.day07a import process_date


def solve(task: str) -> int:
    """Compute how many IPs support TLS."""
    count = 0
    ips = process_date(task)
    for ip in ips:
        if ip.support_ssl:
            count += 1
    return count
