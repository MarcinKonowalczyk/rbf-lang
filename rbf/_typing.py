"""
Typing imports helper so we don't need to write all of this in every file.
"""

try:
    from beartype.typing import (
        Sequence,
        Union,
        Callable,
        Optional,
        TYPE_CHECKING,
    )
except ImportError:
    from typing import (
        Sequence,
        Union,
        Callable,
        Optional,
        TYPE_CHECKING,
    )

if TYPE_CHECKING:
    from typing_extensions import overload
else:

    def overload(func):
        return func
