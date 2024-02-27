from typing import Sequence, Union
from typing_extensions import overload

from .command import Command


class Program(Sequence[Command]):
    """RBF program."""

    def __init__(self, program: Union[str, Sequence[Command]]) -> None:
        program = validate_program(program)
        self.program = program
        self.size = len(program)
        self.pointer = 0
        self.steps = 0

    def __len__(self) -> int:
        return self.size

    @overload
    def __getitem__(self, index: int) -> Command: ...

    @overload
    def __getitem__(self, index: slice) -> Sequence[Command]: ...

    def __getitem__(
        self, index_or_slice: Union[int, slice]
    ) -> Union[Command, Sequence[Command]]:
        if isinstance(index_or_slice, int):
            return self.program[index_or_slice]
        elif isinstance(index_or_slice, slice):
            return self.program[index_or_slice]
        else:
            raise TypeError("Index must be an int or a slice.")

    def _single_char_repr(self) -> str:
        return "".join(command.value for command in self.program)

    def __repr__(self) -> str:
        return f"Program({self._single_char_repr()!r})"

    def __str__(self) -> str:
        return self._single_char_repr()

    def move_right(self) -> None:
        """Move the program pointer to the right."""
        if self.pointer < self.size - 1:
            self.pointer += 1
        else:
            raise ValueError(
                f"Program pointer out of bounds at {self.pointer} (size: {self.size})."
            )

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
                if self.program[self.pointer] == Command.LOOP_START:
                    bracket_depth += 1
                elif self.program[self.pointer] == Command.LOOP_END:
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
                if self.program[self.pointer] == Command.LOOP_START:
                    bracket_depth -= 1
                elif self.program[self.pointer] == Command.LOOP_END:
                    bracket_depth += 1

                if self.pointer == 0:
                    raise ValueError("Unmatched loop end.")

    def reset(self) -> None:
        """Reset the program."""
        self.pointer = 0
        self.steps = 0

    @property
    def current_command(self) -> Command:
        return self.program[self.pointer]


def validate_program(program: Union[str, Sequence[Command]]) -> Sequence[Command]:
    """Validate the RBF program."""

    parsed_commands: Sequence[Command]
    if isinstance(program, str):
        # Convert the string to a list of Commands.
        parsed_commands = [Command(command) for command in program]
    else:
        # The program is already a list of Commands.
        parsed_commands = program

    bracket_depth = 0  # Keep track of the depth of the brackets.
    for command in parsed_commands:
        if command == Command.LOOP_START:
            bracket_depth += 1
        elif command == Command.LOOP_END:
            bracket_depth -= 1

        if bracket_depth < 0:
            raise ValueError("Unmatched loop end.")

    if bracket_depth != 0:
        raise ValueError("Unmatched loop start.")

    return parsed_commands
