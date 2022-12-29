#!/usr/bin/env python3

"""
Only meant to be imported within cog
"""

# Remotes
# To add a new Flatpak source (with Flathub as the example):
#
# flatpak remote-add --user --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo
# To delete an existing Flathub source:
#
# flatpak remote-delete --user flathub


def install_flatpak(appid: str, remote: str) -> str:
    return f"flatpak install {remote} {appid}"


def remove_flatpak(appid: str, remote: str, delete_data: bool = True) -> str:
    delete_cmd = " --delete-data" if delete_data else ""
    return f"flatpak uninstall {appid} {delete_cmd}"


def ver_cmd(pkg: str, grep: str) -> str:
    return rf'printf "{pkg} > %s\n" "$(apt-cache policy {pkg} | grep {grep} | cut -d: -f2 | tr -d /" /")"'


def flatpak_upstream_ver_cmd(appid: str, remote: str) -> str:
    return rf'printf "{appid} > %s\n" "$(flatpak search {appid} | head -n1 | cut -f4 | tr -d /" /")"'


def flatpak_local_ver_cmd(appid: str, remote: str) -> str:
    return rf'printf "{appid} > %s\n" "$(flatpak info {appid} | grep Version | cut -d: -f2 | tr -d /" /")"'
