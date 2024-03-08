"""
Reversible BitFuck (RBF) interpretor
"""

__version__ = "0.1.0"

from . import program
from . import tape
from . import runner

Program = program.Program
Tape = tape.Tape
run = runner.run
