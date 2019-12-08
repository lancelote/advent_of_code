"""2019 - Day 2 Part 1: 1202 Program Alarm.

On the way to your gravity assist around the Moon, your ship computer beeps
angrily about a "1202 program alarm". On the radio, an Elf is already
explaining how to handle the situation: "Don't worry, that's perfectly
norma--" The ship computer bursts into flames.

You notify the Elves that the computer's magic smoke seems to have escaped.
"That computer ran Intcode programs like the gravity assist program it was
working on; surely there are enough spare parts up there to build a new
Intcode computer!"

An Intcode program is a list of integers separated by commas
(like 1,0,0,3,99). To run one, start by looking at the first integer
(called position 0). Here, you will find an opcode - either 1, 2, or 99.
The opcode indicates what to do; for example, 99 means that the program is
finished and should immediately halt. Encountering an unknown opcode means
something went wrong.

Opcode 1 adds together numbers read from two positions and stores the result
in a third position. The three integers immediately after the opcode tell you
these three positions - the first two indicate the positions from which you
should read the input values, and the third indicates the position at which
the output should be stored.

For example, if your Intcode computer encounters 1,10,20,30, it should read
the values at positions 10 and 20, add those values, and then overwrite the
value at position 30 with their sum.

Opcode 2 works exactly like opcode 1, except it multiplies the two inputs
instead of adding them. Again, the three integers after the opcode indicate
where the inputs and outputs are, not their values.

Once you're done processing an opcode, move to the next one by stepping
forward 4 positions.

For example, suppose you have the following program:

    1,9,10,3,2,3,11,0,99,30,40,50

For the purposes of illustration, here is the same program split into multiple
lines:

    1,9,10,3,
    2,3,11,0,
    99,
    30,40,50

The first four integers, 1,9,10,3, are at positions 0, 1, 2, and 3. Together,
they represent the first opcode (1, addition), the positions of the two inputs
(9 and 10), and the position of the output (3). To handle this opcode, you
first need to get the values at the input positions: position 9 contains 30,
and position 10 contains 40. Add these numbers together to get 70. Then, store
this value at the output position; here, the output position (3) is at
position 3, so it overwrites itself. Afterward, the program looks like this:

    1,9,10,70,
    2,3,11,0,
    99,
    30,40,50

Step forward 4 positions to reach the next opcode, 2. This opcode works just
like the previous, but it multiplies instead of adding. The inputs are at
positions 3 and 11; these positions contain 70 and 50 respectively.
Multiplying these produces 3500; this is stored at position 0:

    3500,9,10,70,
    2,3,11,0,
    99,
    30,40,50

Stepping forward 4 more positions arrives at opcode 99, halting the program.

Here are the initial and final states of a few more small programs:

    1,0,0,0,99 becomes 2,0,0,0,99 (1 + 1 = 2).
    2,3,0,3,99 becomes 2,3,0,6,99 (3 * 2 = 6).
    2,4,4,5,99,0 becomes 2,4,4,5,99,9801 (99 * 99 = 9801).
    1,1,1,4,99,5,6,0,99 becomes 30,1,1,4,2,5,6,0,99.

Once you have a working computer, the first step is to restore the gravity
assist program (your puzzle input) to the "1202 program alarm" state it had
just before the last computer caught fire. To do this, before running the
program, replace position 1 with the value 12 and replace position 2 with the
value 2. What value is left at position 0 after the program halts?
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List


@dataclass
class Computer:
    """Intcode computer.

    Stores program in memory as a list of integer and the current opcode under
    execution index.
    """

    memory: List[int] = field(default_factory=list)
    instruction_pointer: int = 0

    def load_program(self, string: str):
        """Load program to memory."""
        self.memory = [int(opcode) for opcode in string.split(',')]

    def next(self):
        """Get the next instruction and increment the pointer."""
        opcode = self.memory[self.instruction_pointer]
        self.instruction_pointer += 1
        return opcode

    def sum(self):
        """Sum next opcodes.

        1. Get two next opcodes.
        2. Treat them as indexes.
        3. Get new two opcodes by the given indexes from the previous step.
        4. Sum opcodes from the previous step.
        5. Get new next opcode.
        6. Treat it as index.
        7. Store the sum by the given index from the previous step.
        """
        address1 = self.instruction_pointer
        address2 = self.instruction_pointer + 1
        address3 = self.instruction_pointer + 2

        param1 = self.memory[address1]
        param2 = self.memory[address2]
        param3 = self.memory[address3]

        self.memory[param3] = self.memory[param1] + self.memory[param2]
        self.instruction_pointer += 3

    def multiply(self):
        """Multiply next opcodes.

        1. Get two next opcodes.
        2. Treat them as indexes.
        3. Get new two opcodes by the given indexes from the previous step.
        4. Multiply opcodes from the previous step.
        5. Get new next opcode.
        6. Treat it as index.
        7. Store the multiplication result by the given index.
        """
        address1 = self.instruction_pointer
        address2 = self.instruction_pointer + 1
        address3 = self.instruction_pointer + 2

        param1 = self.memory[address1]
        param2 = self.memory[address2]
        param3 = self.memory[address3]

        self.memory[param3] = self.memory[param1] * self.memory[param2]
        self.instruction_pointer += 3

    def execute(self):
        """Iterate over opcodes in memory executing commands unless 99 stop."""
        assert self.memory, "no program loaded."

        while True:
            opcode = self.next()
            if opcode == 1:
                self.sum()
            elif opcode == 2:
                self.multiply()
            elif opcode == 99:
                break
            else:
                raise ValueError('')


def solve(task: str) -> int:
    """Execute a program and return 0 index opcode."""
    computer = Computer()
    computer.load_program(task)
    computer.memory[1] = 12
    computer.memory[2] = 2

    computer.execute()

    return computer.memory[0]
