"""2025 - Day 8 Part 1: Playground"""

from src.year2025.day08a import Box
from src.year2025.day08a import get_junctions
from src.year2025.day08a import process_data


def solve(task: str) -> int:
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

    while True:
        _, a, b = junctions.pop()
        connect(a, b)
        if len(circuits) == 1:
            return a[0] * b[0]
