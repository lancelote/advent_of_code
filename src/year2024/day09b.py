"""2024 - Day 9 Part 2: Disk Fragmenter"""

from __future__ import annotations

from abc import abstractmethod
from abc import ABC
from dataclasses import dataclass


@dataclass
class Object(ABC):
    pk: int
    ptr: int
    length: int

    @abstractmethod
    def append_to(self, memory: Memory) -> None:
        pass


@dataclass
class File(Object):
    def append_to(self, memory: Memory) -> None:
        for _ in range(self.length):
            memory.append(self.pk)

    def move_to(self, memory: Memory, at: int) -> None:
        for i in range(self.length):
            # copy to new position
            memory.data[at + i] = self.pk

            # remove from old position
            memory.data[self.ptr + self.length - i - 1] = None


@dataclass
class Space(Object):
    def append_to(self, memory: Memory) -> None:
        for _ in range(self.length):
            memory.append(None)


class Memory:
    def __init__(self) -> None:
        self.data: list[int | None] = []
        self.files: list[File] = []
        self.spaces: list[Space] = []

    def read_line(self, line: str) -> None:
        for i in range(0, len(line), 2):
            file = File(pk=i // 2, ptr=len(self.data), length=int(line[i]))
            file.append_to(memory=self)
            self.files.append(file)

            if i + 1 < len(line):
                space = Space(
                    pk=i // 2, ptr=len(self.data), length=int(line[i + 1])
                )
                space.append_to(memory=self)
                self.spaces.append(space)

    def append(self, x: int | None) -> None:
        self.data.append(x)

    def compress(self) -> None:
        for file_i in range(len(self.files) - 1, 0, -1):
            file = self.files[file_i]

            for space_i in range(0, file_i):
                space = self.spaces[space_i]

                # not enough space
                if space.length < file.length:
                    continue

                # just enough space
                elif space.length == file.length:
                    file.move_to(self, at=space.ptr)
                    space.length = 0
                    break

                # more than enough space
                else:
                    file.move_to(self, at=space.ptr)
                    space.ptr += file.length
                    space.length -= file.length
                    break

    @property
    def checksum(self) -> int:
        return sum(i * x for i, x in enumerate(self.data) if x is not None)

    def __str__(self) -> str:
        return "".join(str(x) if x is not None else "." for x in self.data)


def solve(task: str) -> int:
    memory = Memory()
    memory.read_line(task)
    memory.compress()
    return memory.checksum
