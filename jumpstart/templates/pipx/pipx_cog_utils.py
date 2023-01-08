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
    # return rf'printf "{appid} > %s\n" "$(flatpak search {appid} | head -n1 | cut -f4 | tr -d /" /")"'
    return "# TODO!"


def pipx_local_ver_cmd(package: str, app: str = "", ver: str = "") -> str:
    # return rf'printf "{appid} > %s\n" "$(flatpak info {appid} | grep Version | cut -d: -f2 | tr -d /" /")"'
    return "# TODO!"
