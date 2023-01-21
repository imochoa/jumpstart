#!/usr/bin/env python3

"""
Only meant to be imported within cog
"""

# stdlib imports
from shlex import quote

# 1st party imports
from jumpstart.constants import ENVVARS
from jumpstart.templates.cog_utils import chain_cmds, printf, require_cmds, tempdir_cmd
from jumpstart.templates.cog_utils.constants import VARNAMES
from jumpstart.templates.cog_utils.downloads import download_and_extract

# Getting latest version!
# curl -Ls -o /dev/null -w %{url_effective} https://github.com/cheat/cheat/releases/latest | rev | cut -d/ -f1 | rev


def install_bin(
    url_cmd: str,
    archive_ext: str,
    cmdname: str,
) -> str:
    """ """

    # Download the file
    cmds = download_and_extract(url_cmd=url_cmd, archive_ext=archive_ext)
    # Find file
    cmds += [f"{VARNAMES.SRCFILE}=$(ls . | head -n1)"]
    # change permissions & install it to "cmdname"
    if cmdname:
        cmds += [
            f'sudo chmod +x "${{{VARNAMES.SRCFILE}}}"',
            f'sudo mv "${{{VARNAMES.SRCFILE}}}" "${{{ENVVARS.INSTALL_DST}}}/{quote(cmdname)}"',
        ]

    return chain_cmds(cmds)


if __name__ == "__main__":
    # install_orgrepo(orgrepo="cheat/cheat", filters=["linux", "amd64"])
    pass
