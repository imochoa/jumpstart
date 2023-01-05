#!/usr/bin/env python3

"""
Only meant to be imported within cog
"""

# stdlib imports
import typing as T

# local imports
from .constants import PRINTF_FMT


def str2list(long_string: str) -> list[str]:
    """
    ...since cog only accepts lists
    """
    long_string = long_string.replace('"', "").replace("'", "").strip()
    if not long_string:
        return []
    return [p.strip() for p in long_string.split(",")]


def safedelete(varname: str = "") -> str:
    # [ -f "${BINPATH}" ] && sudo rm "${BINPATH}" || echo "Not installed"
    return r"{varname}=$(mktemp -d -t jumpstart-XXXXXXXXXX)"
