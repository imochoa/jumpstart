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
    # TODO check if URL exists??
    url = f"https://pypi.org/project/{package}/".replace("'", "").replace('"', "")
    ver_cmd = f'curl --silent -JL "{url}" | grep --ignore-case --after-context=2 "release__version\\"" | grep -v --ignore-case "class" | head -n1 | tr -s " "'
    ver_assignment = f"{VARNAMES.VERSION}=$({ver_cmd})"
    ver_print = printf(f"[{package}] version was: ${{{VARNAMES.VERSION}}}")
    return chain_cmds([ver_assignment, ver_print])


def pipx_local_ver_cmd(
    package: str,
) -> str:
    return chain_cmds([f"pipx list | grep installed | grep {package} | ts -s ' ' | cut -d' ' -f8"])
