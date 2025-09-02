"""2016 - Day 2 Part 2: Bathroom Security."""

from src.year2016.day02a import Keypad, processed_data


def solve(task: str) -> str:
    """Find the code for keypad according to instructions given."""
    code = ""
    keypad = Keypad(
        [[1], [2, 3, 4], [5, 6, 7, 8, 9], ["A", "B", "C"], ["D"]], row=2, col=0
    )
    digits = processed_data(task)

    for digit in digits:
        for instruction in digit:
            keypad.move(instruction)
        code += keypad.current_digit

    return code
