"""2017 - Day 6 Part 1: Memory Reallocation."""


class Memory:
    """Memory banks representation."""

    def __init__(self, banks: list[int]) -> None:
        """Each bank is an integer."""
        self.banks = banks

    def redistribute(self) -> None:
        """Take max value and redistribute it equally over all banks."""
        value = max(self.banks)
        index = self.banks.index(value)

        self.banks[index] = 0

        while value:
            value -= 1
            index = (index + 1) % len(self.banks)
            self.banks[index] += 1

    def __str__(self) -> str:
        """Each bank to string separated by space."""
        return " ".join([str(bank) for bank in self.banks])


def solve(task: str) -> int:
    """Find the number of unique redistributions."""
    banks = [int(bank) for bank in task.strip().split()]
    memory = Memory(banks)
    seen: set[str] = set()
    steps = 0

    while str(memory) not in seen:
        seen.add(str(memory))
        memory.redistribute()
        steps += 1

    return steps
