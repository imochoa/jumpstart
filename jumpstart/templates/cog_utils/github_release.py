#!/usr/bin/env python3

"""
Only meant to be imported within cog
"""

# stdlib imports
import typing as T

# local imports
from .utils import require_cmds


def find_latest_ver(orgrepo: str) -> str:
    """
    *orgrepo* should be organization/repository (eg. cheat/cheat)
    """

    # TODO assert curl installed...
    # require_cmds(["curl"])

    return f"curl -Ls -o /dev/null -w %{{url_effective}} https://github.com/{orgrepo}/releases/latest | rev | cut -d/ -f1 | rev"


def find_latest_bin(orgrepo: str, filters: list[str]) -> str:
    """
    *orgrepo* should be organization/repository (eg. cheat/cheat)
    """

    # TODO assert jq installed...
    # require_cmds(["curl"])

    cmd = f"curl --silent https://api.github.com/repos/{orgrepo}/releases/latest | jq '..|.browser_download_url?'"
    cmd += "".join(f" | grep '{f}'" for f in filters)
    return cmd
