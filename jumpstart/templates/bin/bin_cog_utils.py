#!/usr/bin/env python3

"""
Only meant to be imported within cog
"""

# 1st party imports
from jumpstart.templates.cog_utils import require_cmds, tempdir_w_var
from jumpstart.templates.cog_utils.github_release import (
    find_latest_bin,
    find_latest_ver,
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
    if not orgrepo:
        return ""

    cmd = ""
    cmd += require_cmds(["curl", "jq"])

    # Get URL
    url = find_latest_bin(orgrepo=orgrepo, filters=filters)
    cmd += f"URL=$({url})\n"

    # Download to dest

    return cmd


def remove_apt(pkgs: list[str], ppas: list[str]) -> str:
    """
    Don't remove important PPAs!
    """
    if not pkgs:
        raise OSError("No inputs!")
    cmd = ""
    ppas = [ppa for ppa in ppas or [] if ppa not in {"universe", "main"}]
    if ppas:
        cmd += "sudo add-apt-repository --remove " + " ".join(ppas) + "\n"
    return cmd + "sudo apt-get --remove " + " ".join(pkgs)


def ver_cmd(pkg: str, grep: str) -> str:
    return rf'printf "{pkg} > %s\n" "$(apt-cache policy {pkg} | grep {grep} | cut -d: -f2 | tr -d /" /")"'


def apt_upstream_ver_cmd(pkg: str) -> str:
    return ver_cmd(pkg, grep="Candidate")


def apt_local_ver_cmd(pkg: str) -> str:
    return ver_cmd(pkg, grep="Installed")


if __name__ == "__main__":
    install_bin(orgrepo="cheat/cheat", filters=["linux", "amd64"])
