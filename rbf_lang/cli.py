from .runner import run


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("source", help="The source code to run")
    parser.add_argument(
        "-t",
        "--tape",
        help="The initial tape to use. Can be a string of 1s and 0s, or an integer to use as the tape size",
        default="8",
    )
    parser.add_argument(
        "--max-steps",
        type=int,
        help="The maximum number of steps to run",
        default=10_000,
    )
    parser.add_argument(
        "--log-level",
        help="The log level to use",
        default="INFO",
    )

    args = parser.parse_args()

    import logging

    logger = logging.getLogger("rbf")

    logger.setLevel(args.log_level)
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("%(levelname)05s %(name)s: %(message)s"))
    logger.addHandler(handler)

    # Check if tape is a string containing only 1s and 0s
    if all(x in "01" for x in args.tape):
        logger.debug("Using --tape as a string")
        tape = args.tape
    else:
        logger.debug("Using --tape as an integer")
        tape = int(args.tape)

    def callback(program, tape):
        logger.debug(
            f" {program.steps} {program.command.value} {program.pointer:02d} | {tape.pointer:02d} {tape}"
        )
        return False

    _program, tape = run(
        args.source,
        tape,
        max_steps=args.max_steps,
        callback=callback,
    )

    print(tape)
