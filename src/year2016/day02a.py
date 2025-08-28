"""2016 - Day 2 Part 1: Bathroom Security."""


class Keypad:
    """Digital representation of the keypad."""

    def __init__(self, layout: list[list[int | str | None]], row: int = 1, col: int = 1) -> None:
        """Create the keypad representation.

        Args:
            layout (list): A sample keypad layout.
            row (int): Row index of the starter position
            col (int): Column index of the starter position

        Notes:
            Row and column indexes represent not the nested list indexes but
            real life position where some button may not exist but they still
            occupy place

        """
        self.layout = layout
        self.row = row
        self.col = col

        self.complete_layout()

    def move(self, instruction: str, times: int = 1) -> None:
        """Move Up(U), Right(R), Down(D) or Left(L)."""
        for _ in range(times):
            if instruction == "U" and self.can_move_up():
                self.row -= 1
            elif instruction == "R" and self.can_move_right():
                self.col += 1
            elif instruction == "D" and self.can_move_down():
                self.row += 1
            elif instruction == "L" and self.can_move_left():
                self.col -= 1

    def can_move_up(self) -> bool:
        """Check if there is an available button to the top."""
        if self.row == 0:
            return False
        elif self.layout[self.row - 1][self.col] is None:
            return False
        else:
            return True

    def can_move_right(self) -> bool:
        """Check if there is an available button to the right."""
        if self.col == len(self.layout[self.row]) - 1:
            return False
        elif self.layout[self.row][self.col + 1] is None:
            return False
        else:
            return True

    def can_move_down(self) -> bool:
        """Check if there is an available button to the down."""
        if self.row == len(self.layout) - 1:
            return False
        elif self.layout[self.row + 1][self.col] is None:
            return False
        else:
            return True

    def can_move_left(self) -> bool:
        """Check if there is an available button to the left."""
        if self.col == 0:
            return False
        elif self.layout[self.row][self.col - 1] is None:
            return False
        else:
            return True

    def complete_layout(self) -> None:
        """Complete keypad layout to the square one with Nones."""
        longest_row = len(max(self.layout, key=len))
        for i, row in enumerate(self.layout):
            fix = (longest_row - len(row)) // 2
            self.layout[i] = [None] * fix + row + [None] * fix

    @property
    def current_digit(self) -> str:
        """Return the digit on the current position."""
        return str(self.layout[self.row][self.col])


def processed_data(data: str) -> list[list[str]]:
    r"""Convert raw data in the list.

    From: 'UR\nDL'
    To:   [['U', 'R'], ['D', 'L']
    """
    return [list(instruction) for instruction in data.strip().split("\n")]


def solve(task: str) -> str:
    """Find the code for keypad according to instructions given."""
    code = ""
    keypad = Keypad([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    digits = processed_data(task)

    for digit in digits:
        for instruction in digit:
            keypad.move(instruction)
        code += keypad.current_digit

    return code
