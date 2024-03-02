from ._typing import Callable, Optional, Union
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

        command = program.command
        bit = tape.bit

        if command == Command.TOGGLE:
            tape.toggle()
        elif command == Command.TAPE_RIGHT:
            tape.move_right()
        elif command == Command.TAPE_LEFT:
            tape.move_left()
        elif command == Command.LOOP_START:
            program.loop_start(bit)
        elif command == Command.LOOP_END:
            program.loop_end(bit)
        else:
            raise ValueError(f"Unknown command: {command}")

        if program.pointer == len(program) - 1:
            # We've reached the end of the program
            break

        program.move_right()

    return program, tape
