from typing import Sequence, Union
from typing_extensions import overload

_TAPE_SIZE = 8


class Tape(Sequence[bool]):
    """Tape is a circular tape of 1-bit cells. The tape is initialized to all 0s."""

    def __init__(self, size: int = _TAPE_SIZE) -> None:
        self.tape = [False] * size
        self.size = size
        self.pointer = 0

    def __len__(self) -> int:
        return self.size

    @overload
    def __getitem__(self, index: int) -> bool: ...

    @overload
    def __getitem__(self, index: slice) -> Sequence[bool]: ...

    def __getitem__(
        self, index_or_slice: Union[int, slice]
    ) -> Union[bool, Sequence[bool]]:
        if isinstance(index_or_slice, int):
            return self.tape[index_or_slice]
        elif isinstance(index_or_slice, slice):
            return self.tape[index_or_slice]
        else:
            raise TypeError("Index must be an int or a slice.")

    def toggle(self) -> None:
        """Toggle the current cell."""
        self.tape[self.pointer] = not self.tape[self.pointer]

    def move_right(self) -> None:
        """Move the tape head to the right."""
        self.pointer = (self.pointer + 1) % self.size

    def move_left(self) -> None:
        """Move the tape head to the left."""
        self.pointer = (self.pointer - 1) % self.size

    def _single_char_repr(self) -> str:
        return "".join("1" if bit else "0" for bit in self.tape)

    def __repr__(self) -> str:
        return f"Tape({self._single_char_repr()!r})"

    def __str__(self) -> str:
        return self._single_char_repr()

    def reset(self) -> None:
        """Reset the tape to all 0s and move the head to the first cell."""
        self.tape = [False] * self.size
        self.pointer = 0

    @property
    def current_bit(self) -> bool:
        return self.tape[self.pointer]
