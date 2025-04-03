import logging
import argparse
from . import run, Program, Tape


def main() -> None:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--log-level",
        help="The log level to use",
        default="INFO",
    )

    subparsers = parser.add_subparsers(
        required=True,
        dest="subcommand",
    )

    run_parsr = subparsers.add_parser("run", help="Run a source code")

    run_parsr.add_argument("source", help="The source code to run")
    run_parsr.add_argument(
        "-t",
        "--tape",
        help="The initial tape to use. Can be a string of 1s and 0s, or an integer to use as the tape size",
        default="8",
    )
    run_parsr.add_argument(
        "--max-steps",
        type=int,
        help="The maximum number of steps to run",
        default=10_000,
    )

    reverse_parser = subparsers.add_parser("reverse", help="Reverse a source code")

    reverse_parser.add_argument("source", help="The source code to reverse")

    args = parser.parse_args()

    logger = logging.getLogger("rbf")

    logger.setLevel(args.log_level)
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("%(levelname)05s %(name)s: %(message)s"))
    logger.addHandler(handler)

    if args.subcommand == "run":
        run_main(args, logger)
    elif args.subcommand == "reverse":
        reverse_main(args, logger)
    else:
        raise ValueError(f"Unknown subcommand: {args.subcommand}")


def run_main(args: argparse.Namespace, logger: logging.Logger) -> None:
    # Check if tape is a string containing only 1s and 0s
    if all(x in "01" for x in args.tape):
        logger.debug("Using --tape as a string")
        tape = args.tape
    else:
        logger.debug("Using --tape as an integer")
        tape = int(args.tape)

    def callback(program: Program, tape: Tape) -> bool:
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


def reverse_main(args: argparse.Namespace, logger: logging.Logger) -> None:
    from .reverse import reverse_program

    print(reverse_program(args.source))


if __name__ == "__main__":
    main()
