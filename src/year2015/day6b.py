"""Part Two.

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

from src.year2015.day6a import compute_result


def update_light(command, light):
    """Compute new light value.

    Args:
        command (str): 'toggle', 'turn on' or 'turn off'
        light (int): Light status before command execution

    Returns:
        int: New light status
    """
    logic = {
        'toggle': light + 2,
        'turn on': light + 1,
        'turn off': light - 1 if light != 0 else 0
    }
    return logic[command]


def solve(task):
    r"""Total brightness of all lights combined after all instructions.

    Args:
        task (str): turn on 489,959 through 759,964\n...

    Returns:
        int: Total brightness of all lights
    """
    return compute_result(task, update_light)
