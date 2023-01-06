#!/usr/bin/env python3

"""
Only meant to be imported within cog
"""

# 1st party imports
from jumpstart.templates.cog_utils import require_cmds, tempdir_cmd
from jumpstart.templates.cog_utils.github import (
    find_github_release,
    find_github_version,
)

# sudo apt-get install -y curl wget jq
#
# URL=$(curl --silent "https://api.github.com/repos/sharkdp/bat/releases/latest" \
#   | jq '..|.browser_download_url?' | grep 'x86_64' | grep 'linux' | grep 'gnu' \
#   | tr -d '"' )

# curl --silent https://api.github.com/repos/cheat/cheat/releases/latest | jq '..|.browser_download_url?' | grep linux | grep amd64
# "https://github.com/cheat/cheat/releases/download/4.4.0/cheat-linux-amd64.gz"


# Getting latest version!
# curl -Ls -o /dev/null -w %{url_effective} https://github.com/cheat/cheat/releases/latest | rev | cut -d/ -f1 | rev


def install_bin(orgrepo: str, filters: list[str]) -> str:
    """ """
    if not orgrepo:
        return ""

    cmd = ""

    # Get URL
    # url = find_github_release(orgrepo=orgrepo, filters=filters)
    # cmd += f"URL=$({url})\n"

    # Download to dest

    return cmd


if __name__ == "__main__":
    install_bin(orgrepo="cheat/cheat", filters=["linux", "amd64"])
