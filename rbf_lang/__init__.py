"""
Reversible BitFuck (RBF) interpretor
"""

__version__ = "0.2.0"

from . import program
from . import tape
from . import runner
from . import reverse

Program = program.Program
Tape = tape.Tape
run = runner.run
reverse_program = reverse.reverse_program
