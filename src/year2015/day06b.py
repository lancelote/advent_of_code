"""2015 - Day 6 Part 1: Probably a Fire Hazard."""

from src.year2015.day06a import compute_result


def update_light(command: str, light: int) -> int:
    """Compute new light value.

    Args:
        command (str): 'toggle', 'turn on' or 'turn off'
        light (int): Light status before command execution

    Returns:
        int: New light status
    """
    logic = {
        "toggle": light + 2,
        "turn on": light + 1,
        "turn off": light - 1 if light != 0 else 0,
    }
    return logic[command]


def solve(task: str) -> int:
    r"""Total brightness of all lights combined after all instructions.

    Args:
        task (str): turn on 489,959 through 759,964\n...

    Returns:
        int: Total brightness of all lights

    """
    return compute_result(task, update_light)
