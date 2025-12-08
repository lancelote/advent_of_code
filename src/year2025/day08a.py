"""2025 - Day 8 Part 1: Playground"""

import math

type Box = tuple[int, int, int]
type Circuits = dict[int, set[Box]]
type Distance = float
type Junction = tuple[Distance, Box, Box]


def process_data(data: str) -> list[Box]:
    boxes: list[Box] = []

    for line in data.splitlines():
        a, b, c = line.split(",")
        box = (int(a), int(b), int(c))
        boxes.append(box)

    return boxes


def get_distance(a: Box, b: Box) -> Distance:
    x1, y1, z1 = a
    x2, y2, z2 = b

    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def get_junctions(boxes: list[Box]) -> list[Junction]:
    junctions: list[Junction] = []

    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            a = boxes[i]
            b = boxes[j]
            d = get_distance(a, b)
            junctions.append((d, a, b))

    return junctions


def three_largest_multiplied(circuits: Circuits) -> int:
    lens = [len(x) for x in circuits.values()]
    lens = sorted(lens, reverse=True)
    a, b, c = lens[:3]
    return a * b * c


def solve_with(task: str, n_connections: int) -> int:
    boxes = process_data(task)
    junctions = get_junctions(boxes)
    junctions.sort(reverse=True)

    circuits = {i: {b} for i, b in enumerate(boxes)}
    box_to_id = {b: i for i, b in enumerate(boxes)}
    box_id_to_circuit_id = list(range(len(boxes)))

    def get_circuit_id(b0: Box) -> int:
        b0_id = box_to_id[b0]

        pk = box_id_to_circuit_id[b0_id]
        while box_id_to_circuit_id[pk] != pk:
            pk = box_id_to_circuit_id[pk]

        return pk

    def update_circuit(b0: Box, new_circuit_id: int) -> None:
        b0_circuit_id = get_circuit_id(b0)

        if b0_circuit_id == new_circuit_id:
            return  # already in the same circuit

        circuits[new_circuit_id].update(circuits[b0_circuit_id])
        del circuits[b0_circuit_id]
        box_id_to_circuit_id[b0_circuit_id] = new_circuit_id

    def connect(b1: Box, b2: Box) -> None:
        b1_circuit = get_circuit_id(b1)
        update_circuit(b2, b1_circuit)

    for _ in range(n_connections):
        _, a, b = junctions.pop()
        connect(a, b)

    return three_largest_multiplied(circuits)


def solve(task: str) -> int:
    return solve_with(task, n_connections=1_000)
