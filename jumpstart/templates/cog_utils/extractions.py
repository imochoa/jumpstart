#!/usr/bin/env python3

"""
Only meant to be imported within cog
"""

# stdlib imports
from collections.abc import Callable
from functools import wraps
from shlex import quote as sh_quote
import typing as T
from typing import Any, TypeVar

# 1st party imports
from jumpstart.constants import ARCHIVE_EXTS

# local imports
from .cmds import require_cmds

# R = TypeVar("R")


def log_extractions(func: Callable[[str], list[str]]) -> Callable[[str], list[str]]:
    """Register any function at definition time in
    the 'funcs' dict."""

    # Registers the function during function definition time.
    # func[func.__name__] = func

    @wraps(func)
    def inner(*args: Any, **kwargs: Any) -> Any:
        # TODO add extra logs
        return func(*args, **kwargs)

    return inner


@log_extractions
def extract_zip(p: str) -> list[str]:
    return []


@log_extractions
def extract_tar(p: str) -> list[str]:
    return []


@log_extractions
def extract_targz(p: str) -> list[str]:
    return []


@log_extractions
def extract_gz(p: str) -> list[str]:
    return [f'gzip --decompress "{p}"']


@log_extractions
def extract_7z(p: str) -> list[str]:
    return []


EXTRACTION_FCNS = {
    ARCHIVE_EXTS.ZIP: extract_zip,
    ARCHIVE_EXTS.TAR: extract_tar,
    ARCHIVE_EXTS.TARGZ: extract_targz,
    ARCHIVE_EXTS.GZ: extract_gz,
    ARCHIVE_EXTS.SEVENZ: extract_7z,
}
