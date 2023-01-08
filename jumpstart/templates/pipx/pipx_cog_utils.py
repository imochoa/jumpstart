#!/usr/bin/env python3

"""
Only meant to be imported within cog
"""


def install_pipx_cmd(package: str, app: str = "", ver: str = "") -> str:
    return f"pipx install {package}"


def remove_pipx_cmd(package: str, app: str = "", ver: str = "") -> str:
    # delete_cmd = " --delete-data" if delete_data else ""
    return f"pipx uninstall {package}"


def pipx_upstream_ver_cmd(package: str, app: str = "", ver: str = "") -> str:
    """
    If it's a URL -> Get from github
    If it's a PYPI package -> get with pip
    """
    # IF it's a URL, get from
    # return rf'printf "{appid} > %s\n" "$(flatpak search {appid} | head -n1 | cut -f4 | tr -d /" /")"'
    return "# TODO!"


def pipx_local_ver_cmd(package: str, app: str = "", ver: str = "") -> str:
    return f"pipx list | grep installed | grep {package} | ts -s ' ' | cut -d' ' -f8"
