#!/usr/bin/env python3

"""
Only meant to be imported within cog
"""


def ver_cmd(pkg: str, grep: str) -> str:
    return rf'printf "{pkg} > %s\n" "$(apt-cache policy {pkg} | grep {grep} | cut -d: -f2 | tr -d /" /")"'


def shell_upstream_ver_cmd(pkg: str) -> str:
    return ver_cmd(pkg, grep="Candidate")


def shell_local_ver_cmd(pkg: str) -> str:
    return ver_cmd(pkg, grep="Installed")
