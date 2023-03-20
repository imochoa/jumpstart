#!/usr/bin/env python3

"""
Only meant to be imported within cog
"""
# 1st party imports
from jumpstart.templates.cog_utils import chain_cmds, printf, require_cmds, tempdir_cmd
from jumpstart.templates.cog_utils.constants import ENVVARS, VARNAMES
from jumpstart.templates.cog_utils.downloads import download_and_extract
from jumpstart.templates.cog_utils.utils import safedelete, sh_escape


def install_deb(
    url_cmd: str,
) -> str:
    """ """

    # Download the file
    cmds = download_and_extract(url_cmd=url_cmd, archive_ext="")
    cmds += [f'sudo apt install "{{{VARNAMES.DLFILE}}}"']

    return chain_cmds(cmds)


def remove_deb(
    cmdmap: dict[str, str],
) -> str:
    # TODO
    # sudo apt remove -y {{name}}
    return chain_cmds([safedelete(f"${{{ENVVARS.INSTALL_DST}}}/{v}") for v in cmdmap.values()])


# def ver_cmd(pkg: str, grep: str) -> str:
#     return rf'printf "{pkg} > %s\n" "$(apt-cache policy {pkg} | grep {grep} | cut -d: -f2 | tr -d /" /")"'


def deb_local_ver_cmd() -> str:
    # TODO
    return chain_cmds([])


# VER=$(apt-cache policy "{{name}}" | grep Candidate: | rev | cut -d: -f1 | rev | cut -d- -f1)
# echo "{{"{:>40}".format(name) }} ->  [${VER}]"


def deb_upstream_ver_cmd(
    name: str,
    ver_cmd: str,
    cmdmap: dict[str, str],
) -> str:
    # TODO
    # for k in sorted(cmdmap):
    #     src_cmd = sh_escape(k)
    #     dst_cmd = f"${{{ENVVARS.INSTALL_DST}}}/" + cmdmap[k].strip()
    #     cmds += [
    #         f'sudo chmod +x "{src_cmd}"',
    #         f'sudo mv "{src_cmd}" "{dst_cmd}"',
    #     ]

    cmds = [f"{VARNAMES.VERSION}=$({ver_cmd})", printf(f"{name} > ${{{VARNAMES.VERSION}}}\\n")]

    return chain_cmds(cmds)


# missing=0;
# {#
# Previous approach
# if $(apt list --installed '{{name}}' | grep -q "\[installed\]")
# Now trying
# #}
#
# if [ ! -z $(apt-cache pkgnames | grep '{{name}}') ];
# then
#     echo "[{{ "{:>40}".format(name)  }}] -> [installed!]";
# else
#     echo "[{{ "{:>40}".format(name)  }}] -> [NOT installed!]";
#     missing=1;
# fi

if __name__ == "__main__":
    # url_cmd = r"curl --silent 'https://api.github.com/repos/cheat/cheat/releases/latest' | jq '..|.browser_download_url?' | grep 'linux' | grep 'amd64' | tr -d '\"'"
    # archive_ext = ".GZ",
    # cmdmap={"cheat-*": "cheat"}
    url_cmd = r"curl --silent 'https://api.github.com/repos/ogham/exa/releases/latest' | jq '..|.browser_download_url?' | grep 'linux' | grep 'x86_64' | grep 'musl' | tr -d '\"'"
    archive_ext = ".ZIP"
    cmdmap = {"bin/exa$": "exa"}
    print(
        install_deb(
            url_cmd=url_cmd,
        )
    )
