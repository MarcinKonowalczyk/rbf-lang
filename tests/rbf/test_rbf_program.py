import pytest
import rbf.program
from rbf.program import Program, ProgramMoveError

from rbf.command import Command


def test_run():
    source = "*>" * 8
    program = Program(source)

    assert program == source


def test_hashable():
    source = "*>" * 8
    program = Program(source)
    hash_1 = hash(source)
    hash_2 = hash(program)

    assert hash_1 == hash_2


def test_move():
    source = "*>" * 8
    program = Program(source)

    assert len(program) == 16
    assert program.pointer == 0

    for i in range(15):
        assert program.pointer == i
        program.move_right()

    assert program.steps == 15

    # We now should be at the end of the program
    assert program.pointer == 15
    with pytest.raises(ProgramMoveError):
        program.move_right()

    assert program.pointer == 15
    # This still should have incremented the steps
    assert program.steps == 16

    for i in range(15, 0, -1):
        assert program.pointer == i
        program.move_left()

    assert program.pointer == 0
    assert program.steps == 31

    with pytest.raises(ProgramMoveError):
        program.move_left()

    assert program.steps == 32


def test_reset():
    source = "*>" * 8
    program = Program(source)

    program.move_right()
    program.move_right()
    program.move_right()
    program.move_right()

    assert program.pointer == 4
    assert program.steps == 4

    program.reset()

    assert program.pointer == 0
    assert program.steps == 0


def test_getitem():
    source = "*>" * 8
    program = Program(source)

    assert program[0] == Command("*")
    assert program[1] == Command(">")
    assert program[2] == Command("*")

    assert program[0:3] == [Command("*"), Command(">"), Command("*")]


def test_command_property():
    source = "*>" * 8
    program = Program(source)

    assert program.command == Command("*")
    program.move_right()
    assert program.command == Command(">")


def test_loop_start():
    source = "(*)*"
    program = Program(source)

    # Current bit is 0, so we should jump *past* the matching )
    program.loop_start(False)
    assert program.pointer == 3
    assert program.steps == 1

    program.reset()

    # Current bit is 1, so we should noop (but still increment steps)
    program.loop_start(True)
    assert program.pointer == 0
    assert program.steps == 1


def test_loop_start_overflow():
    source = "(*)"
    program = Program(source)

    # Current bit is 0, so we should jump *past* the matching )
    with pytest.raises(ProgramMoveError):
        program.loop_start(False)
    assert program.pointer == 2
    assert program.steps == 1

    program.reset()

    # Current bit is 1, so we should noop (but still increment steps)
    program.loop_start(True)
    assert program.pointer == 0
    assert program.steps == 1


def test_loop_end():
    source = "(*)*"
    program = Program(source)
    program.move_right()
    program.move_right()

    # Current bit is 0, so we should jump back to just after the matching (
    program.loop_end(False)
    assert program.pointer == 1
    assert program.steps == 3

    program.reset()
    program.move_right()
    program.move_right()

    # Current bit is 1, so we should noop (but still increment steps)
    program.loop_end(True)
    assert program.pointer == 2
    assert program.steps == 3


def test_loop_end_overflow():
    source = "(*)"
    program = Program(source)
    program.move_right()
    program.move_right()

    # Current bit is 0, so we should jump back to just after the matching (
    program.loop_end(False)
    assert program.pointer == 1
    assert program.steps == 3

    program.reset()
    program.move_right()
    program.move_right()

    # Current bit is 1, so we should noop (but still increment steps)
    program.loop_end(True)
    assert program.pointer == 2
    assert program.steps == 3
