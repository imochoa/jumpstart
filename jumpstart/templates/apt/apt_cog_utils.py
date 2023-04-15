#!/usr/bin/env python3

"""
Only meant to be imported within cog
"""


def install_apt(pkgs: list[str], ppas: list[str]) -> str:
    if not pkgs:
        raise OSError("No inputs!")

    cmd = ""
    if ppas:
        cmd += "sudo add-apt-repository -y " + " ".join(ppas) + "\n"
        cmd += "sudo apt-get update -y\n"

    return cmd + "sudo apt-get install -y " + " ".join(pkgs)


def remove_apt(pkgs: list[str], ppas: list[str]) -> str:
    """
    Don't remove important PPAs!
    """
    if not pkgs:
        raise OSError("No inputs!")
    cmd = ""
    ppas = [ppa for ppa in ppas or [] if ppa not in {"universe", "main"}]
    if ppas:
        cmd += "sudo add-apt-repository --remove " + " ".join(ppas) + "\n"
    return cmd + "sudo apt-get remove -y " + " ".join(pkgs)


def ver_cmd(pkg: str, grep: str) -> str:
    return rf'printf "{pkg} > %s\n" "$(apt-cache policy {pkg} | grep {grep} | cut -d: -f2 | tr -d /" /")"'


def apt_upstream_ver_cmd(pkg: str) -> str:
    return ver_cmd(pkg, grep="Candidate")


def apt_local_ver_cmd(pkg: str) -> str:
    return ver_cmd(pkg, grep="Installed")
