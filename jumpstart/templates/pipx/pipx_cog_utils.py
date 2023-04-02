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


def install_pipx(
    package: str,
) -> str:
    """
    app: str = "", ver: str = ""
    """
    return chain_cmds([f"pipx install {package}"])


def remove_pipx(
    package: str,
) -> str:
    """
    app: str = "", ver: str = ""
    """
    # delete_cmd = " --delete-data" if delete_data else ""
    return chain_cmds([f"pipx uninstall {package}"])


def pipx_upstream_ver_cmd(package: str, app: str = "", ver: str = "") -> str:
    """
    If it's a URL -> Get from github
    If it's a PYPI package -> get with pip
    """
    # IF it's a URL, get from
    # return rf'printf "{appid} > %s\n" "$(flatpak search {appid} | head -n1 | cut -f4 | tr -d /" /")"'
    return chain_cmds(["# TODO!"])


def pipx_local_ver_cmd(
    package: str,
) -> str:
    return chain_cmds([f"pipx list | grep installed | grep {package} | ts -s ' ' | cut -d' ' -f8"])
