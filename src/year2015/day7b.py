"""Part Two.

Now, take the signal you got on wire a, override wire b to that signal, and
reset the other wires (including wire a). What new signal is ultimately
provided to wire a?

"""

from src.year2015.day7a import process_data, get_value, HDict


def solve(task):
    r"""Process task data to compute 'a' value after 'b' overriding.

    Function recursively processes task data to compute wire 'a' value
    after wire 'b' signal overriding.

    Args:
        task: "NOT dq -> dr\nkg OR kf -> kh..."

    Returns:
        int: wire 'a' signal value
    """
    commands = process_data(task)
    wires = HDict()

    for command in commands:
        wires[command.output] = command

    wires['b'] = get_value(wires['a'], wires)

    return get_value(wires['a'], wires)
