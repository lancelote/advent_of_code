"""2019 - Day 7 Part 1: Amplification Circuit."""

from itertools import permutations

from src.year2019.intcode import Computer


def compute_output(program: str, phases: tuple[int, ...]) -> int:
    """Compute amplifiers final output."""
    amplifiers = (Computer(), Computer(), Computer(), Computer(), Computer())
    stdin = 0

    for amplifier, phase in zip(amplifiers, phases):
        amplifier.load_program(program)
        amplifier.stdin.append(phase)
        amplifier.stdin.append(stdin)
        amplifier.execute()
        stdin = amplifier.stdout.popleft()

    return stdin


def solve(task: str) -> int:
    """Find max amplifiers output."""
    phase = (0, 1, 2, 3, 4)
    return max(compute_output(task, phases) for phases in permutations(phase))
