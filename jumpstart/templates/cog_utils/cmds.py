#!/usr/bin/env python3

"""
Only meant to be imported within cog
"""

# stdlib imports
import typing as T

# local imports
from .constants import PRINTF_FMT


def chain_cmds(cmds: T.Sequence[str]) -> str:
    return " \\\n    && ".join(cmds)


def require_cmds(cmds: list[str]) -> str:
    """
    Template for when you require some commands
    """
    cmd_str = ""
    for cmd in cmds:
        cmd_str += f"if ! command -v '{cmd}' &> /dev/null\n"
        cmd_str += f"then\n"
        cmd_str += f"\techo 'missing!; exit 1'\n"
        cmd_str += f"fi\n\n"

    return cmd_str


def printf(msg: str, fmt: str = PRINTF_FMT) -> str:
    """
    Wrapper for printf
    """
    return f'printf "{fmt}" "{msg}"'


def debug(msg: str) -> str:
    return printf(msg=msg, fmt=r"\e[0;34m%-6s\e[m\n")


def info(msg: str) -> str:
    return printf(msg=msg, fmt=r"\e[0;34m%-6s\e[m\n")


def warn(msg: str) -> str:
    return printf(msg=msg, fmt=r"\e[0;34m%-6s\e[m\n")


def wget(
    url: str,
    dst: str,
    sudo: bool = False,
) -> str:
    """
    Wrapper for wget calls
    """
    prefix = "sudo " if sudo else ""
    return prefix + f'wget "${url}" --continue --output-document="{dst}"'


def tempdir_cmd(varname: str = "", prefix: str = "jumpstart") -> str:
    return f"{varname}=$(mktemp -d -t {prefix}-XXXXXXXXXX)"
