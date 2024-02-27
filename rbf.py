from typing import Sequence, Union
from typing_extensions import overload
import enum

# from dataclasses import dataclass


class RBFCommand(enum.Enum):
    """Enumeration of RBF commands."""

    TOGGLE = "*"
    """Toggle the current bit."""
    TAPE_RIGHT = ">"
    """Shift the tape head right."""

    TAPE_LEFT = "<"
    """Shift the tape head left."""

    LOOP_START = "("
    """If the current bit is zero, jump past matching ). Else, continue (loop)."""

    LOOP_END = ")"
    """If the current bit is zero, jump back to just after matching (. Else, continue."""


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

    def __repr__(self) -> str:
        single_char_tape = "".join("1" if bit else "0" for bit in self.tape)
        return f"Tape({single_char_tape!r})"
    
    @property
    def current_bit(self) -> bool:
        return self.tape[self.pointer]


class Program(Sequence[RBFCommand]):
    """RBF program."""

    def __init__(self, program: Union[str, Sequence[RBFCommand]]) -> None:

        if isinstance(program, str):
            # Convert the string to a list of RBFCommands.
            program = [RBFCommand(command) for command in program]

        self.program = program
        self.size = len(program)
        self.pointer = 0
        self.steps = 0

    def __len__(self) -> int:
        return self.size

    @overload
    def __getitem__(self, index: int) -> RBFCommand: ...

    @overload
    def __getitem__(self, index: slice) -> Sequence[RBFCommand]: ...

    def __getitem__(
        self, index_or_slice: Union[int, slice]
    ) -> Union[RBFCommand, Sequence[RBFCommand]]:
        if isinstance(index_or_slice, int):
            return self.program[index_or_slice]
        elif isinstance(index_or_slice, slice):
            return self.program[index_or_slice]
        else:
            raise TypeError("Index must be an int or a slice.")

    def __repr__(self) -> str:
        single_char_program = "".join(command.value for command in self.program)
        return f"Program({single_char_program!r})"
    
    def move_right(self) -> None:
        """Move the program pointer to the right."""
        if self.pointer < self.size - 1:
            self.pointer += 1
        else:
            raise ValueError(f"Program pointer out of bounds at {self.pointer} (size: {self.size}).")
    
    def move_left(self) -> None:
        """Move the program pointer to the left."""
        if self.pointer > 0:
            self.pointer -= 1
        else:
            raise ValueError("Program pointer out of bounds.")
    
    def loop_start(self, current_bit: bool) -> None:
        """If the current bit is zero, jump past matching ). Else, continue (loop)."""
        if current_bit:
            # The current bit is not zero, so we noop.
            pass
        else:
            # The current bit is zero, so we jump past the matching ).
            bracket_depth = 1
            while bracket_depth > 0:
                self.move_right()
                if self.program[self.pointer] == RBFCommand.LOOP_START:
                    bracket_depth += 1
                elif self.program[self.pointer] == RBFCommand.LOOP_END:
                    bracket_depth -= 1
                
                if self.pointer == self.size - 1:
                    raise ValueError("Unmatched loop start.")

    def loop_end(self, current_bit: bool) -> None:
        """If the current bit is zero, jump back to just after matching (. Else, continue."""
        if current_bit:
            # The current bit is not zero, so we noop.
            pass
        else:
            # The current bit is zero, so we jump back to just after the matching (.
            bracket_depth = 1
            while bracket_depth > 0:
                self.move_left()
                if self.program[self.pointer] == RBFCommand.LOOP_START:
                    bracket_depth -= 1
                elif self.program[self.pointer] == RBFCommand.LOOP_END:
                    bracket_depth += 1

                if self.pointer == 0:
                    raise ValueError("Unmatched loop end.")
    
    @property
    def current_command(self) -> RBFCommand:
        return self.program[self.pointer]

import logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

def run(program: Program, tape: Tape, max_steps: int = 1000) -> None:
    """Run the RBF program."""

    while program.steps < max_steps:
        logger.debug(f"{program.steps=} {program.current_command=}")
        current_command = program.current_command
        current_bit = tape.current_bit

        if current_command == RBFCommand.TOGGLE:
            tape.toggle()
        elif current_command == RBFCommand.TAPE_RIGHT:
            tape.move_right()
        elif current_command == RBFCommand.TAPE_LEFT:
            tape.move_left()
        elif current_command == RBFCommand.LOOP_START:
            program.loop_start(current_bit)
        elif current_command == RBFCommand.LOOP_END:
            program.loop_end(current_bit)
        else:
            raise ValueError(f"Unknown command: {current_command}")

        if program.pointer == program.size - 1:
            break

        program.move_right()
        program.steps += 1

test_program = Program("*>" * 8)
test_tape = Tape()

run(test_program, test_tape)

print(test_tape)

