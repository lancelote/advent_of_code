"""2019 - Day 7 Part 2: Amplification Circuit."""

from itertools import permutations

from src.year2019.intcode import Computer


def compute_output(program: str, phases: tuple[int, ...]) -> int:
    """Compute feedback loop biggest output."""
    amplifiers = (Computer(), Computer(), Computer(), Computer(), Computer())
    stdin = 0

    for amplifier, phase in zip(amplifiers, phases, strict=True):
        amplifier.load_program(program)
        amplifier.stdin.append(phase)
        amplifier.stdin.append(stdin)
        amplifier.execute()
        stdin = amplifier.stdout.popleft()

    while not amplifiers[-1].is_halt:
        for amplifier in amplifiers:
            amplifier.stdin.append(stdin)
            amplifier.execute()
            stdin = amplifier.stdout.popleft()

    return stdin


def solve(task: str) -> int:
    """Find the biggest output."""
    phase = (5, 6, 7, 8, 9)
    return max(compute_output(task, phases) for phases in permutations(phase))
