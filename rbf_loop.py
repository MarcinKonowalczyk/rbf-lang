from rbf.runner import run, Program, Tape
import logging

logging.basicConfig(level=logging.INFO)


def info_message(program: Program, tape: Tape) -> str:
    return f" {program.steps} {program.command.value} {program.pointer:02d} | {tape.pointer:02d} {tape}"


def callback(program: Program, tape: Tape) -> bool:
    logging.info(info_message(program, tape))
    return False


logging.info("Running program")

# Three cells. x, y=0 and f=0
source = """
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
program, tape = run(source, "1000", callback=callback, max_steps=1000)

logging.info(info_message(program, tape))
logging.info("Program finished")
logging.info(f"Tape pointer: {tape.pointer}")
