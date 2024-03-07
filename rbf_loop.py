from rbf.run import run, Program, Tape
import logging

logging.basicConfig(level=logging.INFO)


def info_message(program: Program, tape: Tape) -> str:
    return f" {program.steps} {program.command.value} {program.pointer:02d} | {tape.pointer:02d} {tape}"


def callback(program: Program, tape: Tape) -> bool:
    logging.info(info_message(program, tape))
    return False


logging.info("Running program")

# source = "((*)>)"
source = "*()>>>"
program, tape = run(source, "100", callback=callback, max_steps=10)

logging.info(info_message(program, tape))
logging.info("Program finished")
