import logging
from .run import run

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

test_program = "*>" * 8
tape_size = 8


def callback(program, tape):
    logger.debug(f"Program: {program} | Tape: {tape}")


program, tape = run(
    test_program,
    tape_size,
    callback=callback,
)

print(f"Program: {program}")
print(f"Tape: {tape}")
