from ._typing import Sequence, Union, overload

_TAPE_SIZE = 8


class Tape(Sequence[bool]):
    """Tape is a circular tape of 1-bit cells. The tape is initialized to all 0s."""

    def __init__(self, size: int = _TAPE_SIZE) -> None:
        self._tape = [False] * size
        self._pointer = 0

    def __len__(self) -> int:
        return len(self._tape)

    @property
    def tape(self) -> list[bool]:
        return self._tape

    @property
    def pointer(self) -> int:
        return self._pointer

    @overload
    def __getitem__(self, index: int) -> bool: ...

    @overload
    def __getitem__(self, index: slice) -> Sequence[bool]: ...

    def __getitem__(
        self, index_or_slice: Union[int, slice]
    ) -> Union[bool, Sequence[bool]]:
        if isinstance(index_or_slice, int):
            return self._tape[index_or_slice]
        elif isinstance(index_or_slice, slice):
            return self._tape[index_or_slice]
        else:
            raise TypeError("Index must be an int or a slice.")

    def toggle(self) -> None:
        """Toggle the current cell."""
        self._tape[self._pointer] = not self._tape[self._pointer]

    def move_right(self) -> None:
        """Move the tape head to the right."""
        self._pointer = (self._pointer + 1) % len(self)

    def move_left(self) -> None:
        """Move the tape head to the left."""
        self._pointer = (self._pointer - 1) % len(self)

    def _single_char_repr(self) -> str:
        return "".join("1" if bit else "0" for bit in self._tape)

    def __repr__(self) -> str:
        return f"Tape({self._single_char_repr()!r})"

    def __str__(self) -> str:
        return self._single_char_repr()

    def reset(self) -> None:
        """Reset the tape to all 0s and move the head to the first cell."""
        self._tape = [False] * len(self)
        self._pointer = 0

    @property
    def bit(self) -> bool:
        return self._tape[self._pointer]
