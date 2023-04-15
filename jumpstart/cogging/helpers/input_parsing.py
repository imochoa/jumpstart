#!/usr/bin/env python3

"""
Only meant to be imported within cog
"""

# stdlib imports
import json
import shlex
import typing as T


def sh_escape(s: str) -> str:
    """
    Escape s, but remove the outer single quotes, since often require double quotes

    """
    s = shlex.quote(s)
    if s[0] == s[-1] == "'":
        return s[1:-1]
    return s


def str2list(long_string: str) -> list[str]:
    """
    ...since cog only accepts lists
    """
    long_string = long_string.replace('"', "").replace("'", "").strip()
    if not long_string:
        return []
    return [p.strip() for p in long_string.split(",")]


def str2dict(long_string: str) -> dict[str, str]:
    """
    ...since cog only accepts lists
    """
    return json.loads(long_string.replace("'", '"'))


def safedelete(p: str) -> str:
    """ """
    return f'( [ -f "{p}" ] && sudo rm "{p}" || echo "{p} does not exist" )'
