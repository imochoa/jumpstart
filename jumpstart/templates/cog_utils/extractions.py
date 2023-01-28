#!/usr/bin/env python3

"""
Only meant to be imported within cog
"""
# stdlib imports
from collections.abc import Callable
from functools import wraps
import shlex
from shlex import quote as sh_quote
import typing as T
from typing import Any, TypeVar

# 1st party imports
from jumpstart.constants import ARCHIVE_EXTS

# local imports
from .cmds import printf, require_cmds


def log_extractions(func: Callable[[str], list[str]]) -> Callable[[str], list[str]]:
    """Register any function at definition time in
    the 'funcs' dict."""

    @wraps(func)
    def inner(*args: Any, **kwargs: Any) -> Any:
        # Protect extraction commands
        # args = (shlex.quote(a) for a in args)
        # kwargs = {k: shlex.quote(v) for k, v in kwargs.items()}
        # Add logs
        return [printf(f"Extracting...")] + func(*args, **kwargs) + ['echo "$(ls .)"']

    return inner


@log_extractions
def extract_zip(p: str) -> list[str]:
    """
    Extract and delete *p*
    """
    return [f'unzip "{p}"', f'rm "{p}"']


# TODO GREP INSTEAD OF GLOB! maybe even \grep
# todo: use tar to find paths
# tar -tf bat-v0.22.1-x86_64-unknown-linux-gnu.tar.gz
# FILES
# tar -tf bat-v0.22.1-x86_64-unknown-linux-gnu.tar.gz | grep "bat$"
# DIRECTORIES
# tar -tf bat-v0.22.1-x86_64-unknown-linux-gnu.tar.gz | grep "autocomplete/$"
@log_extractions
def extract_tar(p: str) -> list[str]:
    """
    Extract and delete *p*
    """
    # raise NotImplementedError("ToDo Tar")
    return []


# bat/bin
# cheat/bin
# exa/bin
# fd-find/bin
# neovim/bin-nvim-quickstart

# weird!
# nvm/bin
# BIN DIRS
# pcloud/bin
# pipx/bin
# plantuml/bin


# DEB examples: duf, chrome
@log_extractions
def extract_targz(p: str) -> list[str]:
    """
    Extract and delete *p*
    """
    # Examples to test: lf, jiq
    # tar -xzvf "${TEMPDIR}/data.tar.gz" --directory="${TEMPDIR}" --strip-components=1

    # Handle strip components
    # BEFORETARGZ=$(ls | wc -l)
    # tar -tf $DLFILE | wc -l
    # [ "$(ls | wc -l)" = "${BEFORETARGZ}" ] && echo "same" || echo "differeent"
    # return [f'tar -xzvf "{p}" --strip-components=1']
    return [f'tar -xzvf "{p}"', f'rm "{p}"']


# BTOP++ => TBZ
# tar -xvjf ${BPTOP_TBZ}


@log_extractions
def extract_gz(p: str) -> list[str]:
    """
    Extract and delete *p*
    """
    return [f'gzip --decompress "{p}"']


@log_extractions
def extract_7z(p: str) -> list[str]:
    """
    Extract and delete *p*
    """
    # raise NotImplementedError("ToDo 7Z")
    return []


EXTRACTION_FCNS = {
    ARCHIVE_EXTS.ZIP: extract_zip,
    ARCHIVE_EXTS.TAR: extract_tar,
    ARCHIVE_EXTS.TARGZ: extract_targz,
    ARCHIVE_EXTS.GZ: extract_gz,
    ARCHIVE_EXTS.SEVENZ: extract_7z,
}
