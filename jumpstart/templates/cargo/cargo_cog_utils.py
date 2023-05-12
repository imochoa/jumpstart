#!/usr/bin/env python3

"""
Only meant to be imported within cog
"""

# 1st party imports
from jumpstart.cogging.constants import ENVVARS, VARNAMES
from jumpstart.cogging.helpers import (
    chain_cmds,
    download_and_extract,
    printf,
    require_cmds,
    safedelete,
    sh_escape,
    tempdir_cmd,
)

# Getting latest version!
# curl -Ls -o /dev/null -w %{url_effective} https://github.com/cheat/cheat/releases/latest | rev | cut -d/ -f1 | rev


def install_cargo(
    crate: str,
) -> str:
    """ """

    return chain_cmds([f"cargo install '{crate}'"])


def remove_cargo(
    crate: str,
) -> str:
    return chain_cmds([f"cargo uninstall '{crate}'"])


def cargo_local_ver_cmd() -> str:
    """
    cargo install --list | grep --ignore-case "^just"
    """
    return chain_cmds([])


def cargo_upstream_ver_cmd(
    name: str,
    ver_cmd: str,
    cmdmap: dict[str, str],
) -> str:
    """
    cargo search "just" | head -n1 | cut -d# -f1 | tr -d " "
    """
    # for k in sorted(cmdmap):
    #     src_cmd = sh_escape(k)
    #     dst_cmd = f"${{{ENVVARS.INSTALL_DST}}}/" + cmdmap[k].strip()
    #     cmds += [
    #         f'sudo chmod +x "{src_cmd}"',
    #         f'sudo mv "{src_cmd}" "{dst_cmd}"',
    #     ]

    cmds = [f"{VARNAMES.VERSION}=$({ver_cmd})", printf(f"{name} > ${{{VARNAMES.VERSION}}}\\n")]

    return chain_cmds(cmds)


if __name__ == "__main__":
    print( install_cargo("just") )
