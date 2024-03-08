import enum


class Command(enum.Enum):
    """Enumeration of RBF commands."""

    TOGGLE = "*"
    """Toggle the current bit."""
    TAPE_RIGHT = ">"
    """Shift the tape head right."""

    TAPE_LEFT = "<"
    """Shift the tape head left."""

    LOOP_START = "("
    """If the current bit is zero, jump past matching ). Else, continue (loop)."""

    LOOP_END = ")"
    """If the current bit is zero, jump back to just after matching (. Else, continue."""
