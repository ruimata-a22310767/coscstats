"""Module contains public API functions."""

from typing import Any

from .args import _arg_process


def cosc_args(txt: str) -> dict[str, Any]:
    """Generate statistics for the specified text.

    Args:
      txt:
        The text from which to generate statistics.

    Returns:
      A dictionary containing the generated text statistics.
    """
    if not isinstance(txt, str):
        raise TypeError("`txt` parameter must be a string")

    return {name: stat_func(txt) for name, stat_func in _arg_process().items()}