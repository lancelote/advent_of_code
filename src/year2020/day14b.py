"""2020 - Day 14 Part 2: Docking Data."""

from src.year2020.day14a import Mask
from src.year2020.day14a import Memory
from src.year2020.day14a import Program
from src.year2020.day14a import process_data


class MaskV2(Mask):
    def apply_to(self, value: int) -> list[int]:
        results: list[int] = []
        str_value = f"{value:b}".rjust(36, "0")

        def collect_results(result: str = "", pos: int = 0) -> None:
            rest_value = str_value[pos:]
            rest_mask = self.mask[pos:]

            for i, (bit, mask_bit) in enumerate(
                zip(rest_value, rest_mask, strict=True), start=pos
            ):
                if mask_bit == "X":
                    collect_results(result + "0", i + 1)
                    collect_results(result + "1", i + 1)
                    return
                elif mask_bit == "0":
                    result += bit
                elif mask_bit == "1":
                    result += mask_bit
                else:
                    raise ValueError(f"unexpected mask bit: {mask_bit}")

            results.append(int(result, 2))

        collect_results()
        return results


class MemoryV2(Memory):
    def __init__(self) -> None:
        super().__init__(mask=MaskV2())

    def add(self, address: int, value: int) -> None:
        masked_addresses = self.mask.apply_to(address)
        for masked_address in masked_addresses:
            self.memory[masked_address] = value


def solve(task: str) -> int:
    """Sum all items in memory."""
    commands = process_data(task)
    program = Program(MemoryV2())
    program.execute(commands)
    return program.memory_sum
