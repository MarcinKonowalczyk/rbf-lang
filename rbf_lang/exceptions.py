class RBFError(Exception):
    pass


class ProgramPointerError(RBFError):
    """Raised when the program counter is out of bounds."""


class InvalidProgramError(RBFError):
    """Raised when the program is invalid."""
