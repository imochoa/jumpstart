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


def install_bin(
    url_cmd: str,
    archive_ext: str,
    cmdmap: dict[str, str],
) -> str:
    """ """

    # Download the file
    cmds = download_and_extract(url_cmd=url_cmd, archive_ext=archive_ext)
    # Find file
    # cmds += [f"{VARNAMES.SRCFILE}=$(ls . | head -n1)"]
    # # change permissions & install it to "cmdname"

    # for k in sorted(cmdmap):
    #     src_cmd = sh_escape(k)
    #     # TODO add globbing?
    #     # dst_cmd = f"${{{ENVVARS.INSTALL_DST}}}/" + v or src_cmd.split('/')[-1]
    #     dst_cmd = f"${{{ENVVARS.INSTALL_DST}}}/" + cmdmap[k].strip()
    #     cmds += [
    #         f'sudo chmod +x "{src_cmd}"',
    #         f'sudo mv "{src_cmd}" "{dst_cmd}"',
    #     ]

    for k in sorted(cmdmap):
        dst = f"${{{ENVVARS.INSTALL_DST}}}/" + cmdmap[k].strip()
        cmds += [
            f"{VARNAMES.SRCPATH}=$( find . -type f | grep --ignore-case '{k}' )",
            f'sudo chmod +x "${{{VARNAMES.SRCPATH}}}"',
            f'sudo mv "${{{VARNAMES.SRCPATH}}}" "{dst}"',
        ]

    return chain_cmds(cmds)


def remove_bin(
    cmdmap: dict[str, str],
) -> str:
    return chain_cmds([safedelete(f"${{{ENVVARS.INSTALL_DST}}}/{v}") for v in cmdmap.values()])


# def ver_cmd(pkg: str, grep: str) -> str:
#     return rf'printf "{pkg} > %s\n" "$(apt-cache policy {pkg} | grep {grep} | cut -d: -f2 | tr -d /" /")"'


def bin_local_ver_cmd() -> str:
    return chain_cmds([])


def bin_upstream_ver_cmd(
    name: str,
    ver_cmd: str,
    cmdmap: dict[str, str],
) -> str:
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
    # url_cmd = r"curl --silent 'https://api.github.com/repos/cheat/cheat/releases/latest' | jq '..|.browser_download_url?' | grep 'linux' | grep 'amd64' | tr -d '\"'"
    # archive_ext = ".GZ",
    # cmdmap={"cheat-*": "cheat"}
    url_cmd = r"curl --silent 'https://api.github.com/repos/ogham/exa/releases/latest' | jq '..|.browser_download_url?' | grep 'linux' | grep 'x86_64' | grep 'musl' | tr -d '\"'"
    archive_ext = ".ZIP"
    cmdmap = {"bin/exa$": "exa"}
    print(
        install_bin(
            url_cmd=url_cmd,
            archive_ext=archive_ext,
            cmdmap=cmdmap,
        )
    )
