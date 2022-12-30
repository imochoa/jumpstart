#!/usr/bin/env python3

"""
Only meant to be imported within cog
"""

# stdlib imports
import typing as T


def require_cmds(cmds: list[str]) -> str:
    """
    Template for when you require some commands
    """
    cmd_str = ""
    for cmd in cmds:
        cmd_str += f"if ! command -v '{cmd}' &> /dev/null\n"
        cmd_str += f"then\n"
        cmd_str += f"\techo 'missing!'\n"
        cmd_str += f"fi\n\n"

    return cmd_str


def str2list(long_string: str) -> list[str]:
    """
    ...since cog only accepts lists
    """
    long_string = long_string.replace('"', "").replace("'", "").strip()
    if not long_string:
        return []
    return [p.strip() for p in long_string.split(",")]


def tempdir_w_var(varname: str = "") -> str:
    return f"{varname}=$(mktemp -d -t jumpstart-XXXXXXXXXX)\n"


def safedelete(varname: str = "") -> str:
    # [ -f "${BINPATH}" ] && sudo rm "${BINPATH}" || echo "Not installed"
    return f"{varname}=$(mktemp -d -t jumpstart-XXXXXXXXXX)\n"
