#!/usr/bin/env python3

"""
Only meant to be imported within cog
"""

# stdlib imports
import typing as T

# 1st party imports
from jumpstart.cogging.constants import ENVVARS, PRINTF_FMT


def chain_cmds(cmds: T.Sequence[str]) -> str:
    return " \\\n&& ".join(cmds)


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


def tempdir_cmd(varname: str = "", prefix: str = "jumpstart") -> str:
    return f"{varname}=$(mktemp -d -t {prefix}-XXXXXXXXXX)"


def env_defaults(
    install_dst: str,
) -> str:
    """ """
    return "\n".join(
        (
            # f'{ENVVARS.INSTALL_DST}="${{{ENVVARS.INSTALL_DST}:-{install_dst}}}"',
            # f'{ENVVARS.BASHCOMP_P}="${{{ENVVARS.BASHCOMP_P}:-${{HOME}}/.config/bash/bash_completion}}"',
            # r'ZSHCOMP="${ZSHCOMP:-${HOME}/.config/zsh/completions}"',
            # r'TEMPDIR="$(mktemp -d -t XXXXXXXXXX)"',
            # r"FMT='\e[0;34m%-6s\e[m\n'",
        )
    )
