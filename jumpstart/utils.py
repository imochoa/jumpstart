#!/usr/bin/env python3


out = \
    """
    aptitude:
      Installed: 0.8.13-3ubuntu1
      Candidate: 0.8.13-3ubuntu1
      Version table:
     *** 0.8.13-3ubuntu1 500
            500 http://de.archive.ubuntu.com/ubuntu jammy/universe amd64 Packages
            100 /var/lib/dpkg/status
    """

print("do!")
import subprocess

pkgs = ["aptitude", "poop"]
p = subprocess.run(["apt-cache", "policy"] + pkgs, capture_output=True)
stdout_lines = p.stdout.decode('utf-8').splitlines()

local_map=dict()
upstream_map=dict()

for pkg in pkgs:
    title = f"{pkg}:"
    try:
        idx = next(idx for idx, l in enumerate(stdout_lines) if l == title)
    except StopIteration:
        continue
    local_ver_idx = idx + 1
    upstream_ver_idx = idx + 2

    def get_ver(idx: int) -> str:
        return ' '.join(stdout_lines[idx].split(":")[1:]).strip()

    local_map[pkg]= get_ver(idx + 1)
    upstream_map[pkg]= get_ver(idx + 2)

print("hoho")

