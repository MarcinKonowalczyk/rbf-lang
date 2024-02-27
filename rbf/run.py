from typing import Union, Callable, Optional

from .command import Command
from .program import Program
from .tape import Tape


def run(
    program: Union[str, Program],
    tape: Union[int, Tape],
    max_steps: int = 1000,
    callback: Optional[Callable[[Program, Tape], bool]] = None,
) -> tuple[Program, Tape]:
    """Run the RBF program. The program will run until it reaches the maximum number of steps or the callback returns True."""

    if isinstance(program, str):
        program = Program(program)

    if isinstance(tape, int):
        tape = Tape(size=tape)

    while program.steps < max_steps:
        # Run the callback and break if it returns True
        if callback and callback(program, tape):
            break

        current_command = program.current_command
        current_bit = tape.current_bit

        if current_command == Command.TOGGLE:
            tape.toggle()
        elif current_command == Command.TAPE_RIGHT:
            tape.move_right()
        elif current_command == Command.TAPE_LEFT:
            tape.move_left()
        elif current_command == Command.LOOP_START:
            program.loop_start(current_bit)
        elif current_command == Command.LOOP_END:
            program.loop_end(current_bit)
        else:
            raise ValueError(f"Unknown command: {current_command}")

        if program.pointer == program.size - 1:
            break

        program.move_right()
        program.steps += 1

    return program, tape
