#!/usr/bin/env python3

"""
Only meant to be imported within cog
"""

# 1st party imports
from jumpstart.cogging.constants import VARNAMES
from jumpstart.cogging.helpers.extracting import EXTRACTION_FCNS
from jumpstart.cogging.helpers.shell_code import (
    chain_cmds,
    printf,
    require_cmds,
    tempdir_cmd,
)
from jumpstart.constants import ARCHIVE_EXTS


def wget(
    url: str,
    dst: str,
    add_ext: bool = True,
    as_root: bool = False,
) -> str:
    """
    Wrapper for wget calls
    """
    sudo = "sudo " if as_root else ""
    url = url.replace('"', "")
    dst = dst.replace('"', "")
    if add_ext:
        dst = f"{dst}.{url.split('.')[-1]}"
    return sudo + f'wget "{url}" --continue --output-document="{dst}"'


def curl(
    url: str,
    dst: str,
    add_ext: bool = True,
    as_root: bool = False,
) -> str:
    """
    Wrapper for curl calls
    """
    url = url.replace('"', "")
    dst_cmd = ""
    dst = dst.strip()
    if dst:
        dst = dst.replace('"', "").replace("'", "")
        if add_ext:
            dst = f"{dst}.{url.split('.')[-1]}"
        dst_cmd = f' -o "{dst}"'

    sudo = "sudo " if as_root else ""
    return sudo + f'curl -JL "{url}"' + dst_cmd


def download_and_extract(
    url_cmd: str,
    archive_ext: str,
) -> list[str]:
    """
    Downloads file using *url_cmd* and applies the extraction operation specified by *archive_ext*
    Saves the result in the variable named *VARNAMES.DLFILE*
    """
    exts_tuple: tuple[str, ...] = getattr(ARCHIVE_EXTS, archive_ext, tuple())

    cmds = [
        tempdir_cmd(VARNAMES.TMPDIR),
        f'cd "${{{VARNAMES.TMPDIR}}}"',
        printf(f"Downloading to $(realpath .)"),
        f"{VARNAMES.URL}=$({url_cmd})",
        f'curl -jLO "${{{VARNAMES.URL}}}"',
        f"{VARNAMES.DLFILE}=$(ls . | head -n1)",
    ]

    if exts_tuple:
        cmds += EXTRACTION_FCNS[exts_tuple](f"${{{VARNAMES.DLFILE}}}")

    return cmds


if __name__ == "__main__":
    print(
        wget(
            url="https://raw.githubusercontent.com/neovim/neovim.github.io/master/logos/neovim-mark.svg",
            dst="/tmp/hoho",
        ),
    )

    url_cmd = "curl --silent 'https://api.github.com/repos/cheat/cheat/releases/latest' | jq '..|.browser_download_url?' | grep 'linux' | grep 'amd64' | tr -d '\"'"
    print(chain_cmds(download_and_extract(url_cmd, archive_ext="GZ")))
    print("done!")
