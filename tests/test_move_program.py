from rbf.runner import run


def test_move_bit() -> None:
    move_right = """
    # Move the bit under the pointer to the right, using a temporary cell
    # x=?, y=0, f=0
    (>>*<<) # set f if x is set
    >>( # if f is set
        <(>*<)* # set y
        <*(>>*<<) # unset x
    >>)
    <(>*<) # if y is set, unset f
    (>>*<<)>>(<(>*<)*<*(>>*<<)>>)<(>*<)
    (>>*<<)>>(<(>*<)*<*(>>*<<)>>)<(>*<)
    (>>*<<)>>(<(>*<)*<*(>>*<<)>>)<(>*<)
    """

    program, tape = run(move_right, "100")

    assert program.steps == 100
    assert tape == "010"
    program.reset()
    program, tape = run(program, tape)

    assert program.steps == 100
    assert tape == "001"
