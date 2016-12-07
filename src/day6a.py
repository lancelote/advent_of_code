# coding=utf-8

"""
--- Day 6: Probably a Fire Hazard ---

Because your neighbors keep defeating you in the holiday house decorating
contest year after year, you've decided to deploy one million lights in a
1000x1000 grid.

Furthermore, because you've been especially nice this year, Santa has mailed
you instructions on how to display the ideal lighting configuration.

Lights in your grid are numbered from 0 to 999 in each direction; the lights
at each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include
whether to turn on, turn off, or toggle various inclusive ranges given as
coordinate pairs. Each coordinate pair represents opposite corners of a
rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers
to 9 lights in a 3x3 square. The lights all start turned off.

To defeat your neighbors this year, all you have to do is set up your lights
by doing the instructions Santa sent you in order.

For example:

    turn on 0,0 through 999,999 would turn on (or leave on) every light.

    toggle 0,0 through 999,0 would toggle the first line of 1000 lights,
    turning off the ones that were on, and turning on the ones that were off.

    turn off 499,499 through 500,500 would turn off (or leave off) the middle
    four lights.

After following the instructions, how many lights are lit?
"""

import re
from collections import namedtuple

PATTERN = re.compile(r'([a-z ]*) ([\d,]*) through ([\d,]*)')


def process_data(data):
    """Process row data into list of namedtuples

    Args:
        data (str): turn on 489,959 through 759,964\n...

    Returns:
        lst: [namedtuple(command, start, end), ...] where start and end are
            coordinates namedtuple(x, y)
    """
    processed_data = []
    coordinates = namedtuple('Coordinates', ['x', 'y'])
    instruction = namedtuple('Instruction', ['command', 'start', 'end'])

    for string in data.strip().split('\n'):
        command, start, end = re.match(PATTERN, string).groups()
        start = coordinates(*map(int, start.split(',')))
        end = coordinates(*map(int, end.split(',')))
        processed_data.append(instruction(command, start, end))

    return processed_data


def update_light(command, light):
    """
    Compute new light status

    Args:
        command (str): 'toggle', 'turn on' or 'turn off'
        light (bool): Light status before command execution

    Returns:
        bool: New light status
    """
    logic = {
        'toggle': not light,
        'turn on': True,
        'turn off': False
    }
    return logic[command]


def compute_result(task, execute):
    """Calculate number of powered lights after all instructions

    Args:
        execute (function): Returns new light status after given command and
            previous light status
        task (str): turn on 489,959 through 759,964\n...

    Returns:
        int: Number of powered lights
    """
    instructions = process_data(task)
    lights = [[False]*1000 for _ in range(1000)]

    for instruction in instructions:
        for i in range(instruction.start.x, instruction.end.x + 1):
            for j in range(instruction.start.y, instruction.end.y + 1):
                lights[i][j] = execute(instruction.command, lights[i][j])

    return sum(light for row in lights for light in row)


def solve(task):
    """Calculate number of powered lights after all instructions

    Args:
        task (str): turn on 489,959 through 759,964\n...

    Returns:
        int: Number of powered lights
    """
    return compute_result(task, update_light)
