#!/usr/bin/env python3

"""
Only meant to be imported within cog
"""


def add_pkgs(pkgs: list[str]) -> str:
    if not pkgs:
        raise OSError("No inputs!")
    return "sudo apt-get install -y " + " ".join(pkgs)


def remove_pkgs(pkgs: list[str]) -> str:
    if not pkgs:
        raise OSError("No inputs!")
    return "sudo apt-get --remove " + " ".join(pkgs)


def add_ppas(ppas: list[str]) -> str:
    if not ppas:
        return ""
    return "sudo add-apt-repository -y " + " ".join(ppas) + "\nsudo apt-get update -y"


def remove_ppas(ppas: list[str]) -> str:
    """
    Don't remove important PPAs!
    """
    ppas = [ppa for ppa in ppas if ppa not in {"universe", "main"}]
    if not ppas:
        return ""
    return "sudo add-apt-repository --remove " + " ".join(ppas)


def ver_cmd(pkg: str, grep: str) -> str:
    return rf'printf "{pkg} > %s\n" "$(apt-cache policy {pkg} | grep {grep} | cut -d: -f2 | tr -d /" /")"'


def shell_upstream_ver_cmd(pkg: str) -> str:
    return ver_cmd(pkg, grep="Candidate")


def shell_local_ver_cmd(pkg: str) -> str:
    return ver_cmd(pkg, grep="Installed")
