"""2022 - Day 10 Part 2: Cathode-Ray Tube."""
from src.year2022.day10a import CPU


def print_screen(screen: list[list[str]]) -> None:
    print("\n".join("".join(line) for line in screen))


def solve(task: str) -> int:
    cpu = CPU.from_task(task)
    screen = [["."] * 40 for _ in range(6)]

    for _ in range(40 * 6):
        line_i = (cpu.cycle - 1) // 40
        pixel_i = (cpu.cycle - 1) % 40
        screen[line_i][pixel_i] = "#" if abs(pixel_i - cpu.x) <= 1 else "."
        cpu.step()

    print_screen(screen)
    return -1
