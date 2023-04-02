#!/usr/bin/env python3

"""
Only meant to be imported within cog
"""


def find_github_version(orgrepo: str) -> str:
    """
    *orgrepo* should be organization/repository (eg. cheat/cheat)
    """

    # TODO assert curl installed...
    # require_cmds(["curl"])

    return f"curl -Ls -o /dev/null -w %{{url_effective}} https://github.com/{orgrepo}/releases/latest | rev | cut -d/ -f1 | rev"


def find_github_release(orgrepo: str, filters: list[str]) -> str:
    """
    *orgrepo* should be organization/repository (eg. cheat/cheat)
    requires:
    - curl
    - jq
    """

    cmd = f"curl --silent 'https://api.github.com/repos/{orgrepo}/releases/latest' | jq '..|.browser_download_url?'"
    cmd += "".join(f" | grep '{f}'" for f in filters)
    cmd += " | tr -d '\"'"
    return cmd
