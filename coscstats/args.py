"""Argument validation and processing."""

import sys
from typing import Any, Callable


def _arg_process() -> dict[str, Callable[[str], Any]]:
    """Validate command line arguments and determine corresponding handler functions.

    Returns:
      A dictionary containing the found text statistics functions.
    """
    if sys.version_info < (3, 10):
        from importlib_metadata import entry_points
    else:
        from importlib.metadata import entry_points

    plugin_entrypoints = entry_points(group="coscstats.commands") #TODO: to be reviewed after entrypoint definition

    print(plugin_entrypoints)

    return {ep.name: ep.load() for ep in plugin_entrypoints}