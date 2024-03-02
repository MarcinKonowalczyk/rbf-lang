import rbf.run
from rbf.run import run


def test_run():
    test_program = "*>" * 8
    tape_size = 8

    program, tape = run(
        test_program,
        tape_size,
    )

    assert program == test_program
    assert tape == [0, 0, 0, 0, 0, 0, 0, 0]
