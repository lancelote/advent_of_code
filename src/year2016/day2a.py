"""Day 2: Bathroom Security.

You arrive at Easter Bunny Headquarters under cover of darkness. However, you
left in such a rush that you forgot to use the bathroom! Fancy office buildings
like this one usually have keypad locks on their bathrooms, so you search the
front desk for the code.

"In order to improve security," the document you find says, "bathroom codes
will no longer be written down. Instead, please memorize and follow the
procedure below to access the bathrooms."

The document goes on to explain that each button to be pressed can be found by
starting on the previous button and moving to adjacent buttons on the keypad:
U moves up, D moves down, L moves left, and R moves right. Each line of
instructions corresponds to one button, starting at the previous button (or,
for the first line, the "5" button); press whatever button you're on at the end
of each line. If a move doesn't lead to a button, ignore it.

You can't hold it much longer, so you decide to figure out the code as you walk
to the bathroom. You picture a keypad like this:

    1 2 3
    4 5 6
    7 8 9

Suppose your instructions are:

    ULL
    RRDDD
    LURDL
    UUUUD

  - You start at "5" and move up (to "2"), left (to "1"), and left (you can't,
    and stay on "1"), so the first button is 1.
  - Starting from the previous button ("1"), you move right twice (to "3") and
    then down three times (stopping at "9" after two moves and ignoring the
    third), ending up with 9.
  - Continuing from "9", you move left, up, right, down, and left, ending
    with 8.
  - Finally, you move up four times (stopping at "2"), then down once, ending
    with 5.

So, in this example, the bathroom code is 1985.

Your puzzle input is the instructions from the document you found at the front
desk. What is the bathroom code?
"""

from typing import List


class Keypad:
    """Digital representation of the keypad."""

    def __init__(self, layout, row=1, col=1) -> None:
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

    def move(self, instruction: str, times=1) -> None:
        """Move Up(U), Right(R), Down(D) or Left(L)."""
        for _ in range(times):
            if instruction == 'U' and self.can_move_up():
                self.row -= 1
            elif instruction == 'R' and self.can_move_right():
                self.col += 1
            elif instruction == 'D' and self.can_move_down():
                self.row += 1
            elif instruction == 'L' and self.can_move_left():
                self.col -= 1

    def can_move_up(self):
        """Check if there is an available button to the top."""
        if self.row == 0:
            return False
        elif self.layout[self.row - 1][self.col] is None:
            return False
        else:
            return True

    def can_move_right(self):
        """Check if there is an available button to the right."""
        if self.col == len(self.layout[self.row]) - 1:
            return False
        elif self.layout[self.row][self.col + 1] is None:
            return False
        else:
            return True

    def can_move_down(self):
        """Check if there is an available button to the down."""
        if self.row == len(self.layout) - 1:
            return False
        elif self.layout[self.row + 1][self.col] is None:
            return False
        else:
            return True

    def can_move_left(self):
        """Check if there is an available button to the left."""
        if self.col == 0:
            return False
        elif self.layout[self.row][self.col - 1] is None:
            return False
        else:
            return True

    def complete_layout(self):
        """Complete keypad layout to the square one with Nones."""
        longest_row = len(max(self.layout, key=len))
        for i, row in enumerate(self.layout):
            fix = (longest_row - len(row)) // 2
            self.layout[i] = [None] * fix + row + [None] * fix

    @property
    def current_digit(self) -> str:
        """Return the digit on the current position."""
        return str(self.layout[self.row][self.col])


def processed_data(data: str) -> List[List[str]]:
    r"""Convert raw data in the list.

    From: 'UR\nDL'
    To:   [['U', 'R'], ['D', 'L']
    """
    return [list(instruction) for instruction in data.strip().split('\n')]


def solve(task: str) -> str:
    """Find the code for keypad according to instructions given."""
    code = ''
    keypad = Keypad([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]])
    digits = processed_data(task)

    for digit in digits:
        for instruction in digit:
            keypad.move(instruction)
        code += keypad.current_digit

    return code
