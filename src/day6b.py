# coding=utf-8

"""
--- Part Two ---

You just finish implementing your winning light pattern when you realize you
mistranslated Santa's message from Ancient Nordic Elvish.

The light grid you bought actually has individual brightness controls; each
light can have a brightness of zero or more. The lights all start at zero.

The phrase turn on actually means that you should increase the brightness of
those lights by 1.

The phrase turn off actually means that you should decrease the brightness of
those lights by 1, to a minimum of zero.

The phrase toggle actually means that you should increase the brightness of
those lights by 2.

What is the total brightness of all lights combined after following Santa's
instructions?

For example:

    turn on 0,0 through 0,0 would increase the total brightness by 1.

    toggle 0,0 through 999,999 would increase the total brightness by 2000000.
"""

from src.day6a import process_data


def solve(task):
    """Calculate total brightness of powered lights after all instructions

    Args:
        task (str): turn on 489,959 through 759,964\n...

    Returns:
        int: Total brightness of powered lights
    """
    instructions = process_data(task)
    lights = [[False]*1000 for _ in range(1000)]

    for instruction in instructions:
        for i in range(instruction.start.x, instruction.end.x + 1):
            for j in range(instruction.start.y, instruction.end.y + 1):
                if instruction.command == 'toggle':
                    lights[i][j] += 2
                elif instruction.command == 'turn on':
                    lights[i][j] += 1
                elif instruction.command == 'turn off':
                    lights[i][j] -= 1 if lights[i][j] != 0 else 0

    return sum(light for row in lights for light in row)
