import pytest
from typing import Any, Generator
from pathlib import Path
import sys


__project_root__ = Path(__file__).resolve().parents[1]
sys.path.append(str(__project_root__))


@pytest.fixture(autouse=True)
def add_space_before_first_print() -> Generator[None, None, None]:
    import builtins

    _print = builtins.print

    def patched_print(*args: Any, **kwargs: Any) -> None:
        _print(end="\n")  # Add a newline
        _print(*args, **kwargs)
        builtins.print = _print

    builtins.print = patched_print
    try:
        yield
    finally:
        builtins.print = _print
