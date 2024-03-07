"""
Typing imports helper so we don't need to write all of this in every file.
"""

from typing import TYPE_CHECKING

if not TYPE_CHECKING:
    try:
        from beartype.typing import (  # noqa: F401
            Sequence,
            Union,
            Callable,
            Optional,
            cast,
        )
    except ImportError:
        from typing import (  # noqa: F401
            Sequence,
            Union,
            Callable,
            Optional,
            cast,
        )
else:
    from typing import (  # noqa: F401
        Sequence,
        Union,
        Callable,
        Optional,
        cast,
    )

if TYPE_CHECKING:
    from typing_extensions import overload
else:

    def overload(func):
        return func
