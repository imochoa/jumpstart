#!/usr/bin/env python3

"""
Only meant to be imported within cog
"""

# stdlib imports
import subprocess
from types import SimpleNamespace

# 3rd party imports
from loguru import logger

# 1st party imports
from jumpstart.templates.cog_utils import chain_cmds, printf, require_cmds, tempdir_cmd
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


def install_orgrepo(
    orgrepo: str,
    filters: list[str],
) -> str:
    """ """
    if not orgrepo:
        return ""

    class VARNAMES(SimpleNamespace):
        """
        Variable names to use in the shell scripts
        """

        TMPDIR = "DLTMP"
        """
        current temporary directory
        """
        DLFILE = "DLFILE"
        """
        Downloaded file (.tar.gz, .zip, ...)
        """
        DLPATH = "DLPATH"
        """
        full path of downloaded file
        """
        URL = "URL"
        """
        URL to download
        """
        SRCFILE = "SRCFILE"
        """
        """
        SRCPATH = "SRCPATH"
        """
        """
        DSTPATH = "SRCPATH"
        """
        """

    URLExts: dict[str, list[str]] = {
        ".tar.gz": [],
        ".gz": [
            f'gzip --decompress "${{{VARNAMES.DLFILE}}}"',
        ],
        ".zip": [],
    }

    # make tmpdir
    # Get URL
    release_url_cmd = find_github_release(orgrepo=orgrepo, filters=filters)

    # Extract
    release_url = subprocess.getoutput(release_url_cmd).replace('"', "").replace("'", "").lower()
    # Extract depending on extension

    passing_exts = [ext for ext in URLExts if release_url.endswith(ext)]
    if not passing_exts:
        logger.error(ValueError(f"unknown extension: {release_url}"))
        return ""
    ext = max(passing_exts, key=len)
    extraction_cmds = URLExts[ext]

    # Build command
    cmdlist = (
        [
            printf("downloading..."),
            tempdir_cmd(VARNAMES.TMPDIR),
            f'cd "${{{VARNAMES.TMPDIR}}}"',
            # f'{VARNAMES.DLFILE}="dl{ext}"',
            # f'{VARNAMES.DLPATH}="${{{VARNAMES.TMPDIR}}}/${{{VARNAMES.DLFILE}}}"',
            f"{VARNAMES.URL}=$({release_url_cmd})",
            f'curl -jLO "${VARNAMES.URL}"',
            rf'{VARNAMES.DLFILE}="$(\ls . )"',
            # f'{VARNAMES.DLPATH}="${{{VARNAMES.TMPDIR}}}/${{{VARNAMES.DLFILE}}}"',
        ]
        + extraction_cmds
        + [
            rf'{VARNAMES.SRCFILE}="$(\ls . )"',
            f'sudo mv "${{{VARNAMES.SRCFILE}}}" ${{INSTALLDIR}}/{{CMDNAME}}',
        ]
    )

    return chain_cmds(cmdlist)


if __name__ == "__main__":
    install_orgrepo(orgrepo="cheat/cheat", filters=["linux", "amd64"])
