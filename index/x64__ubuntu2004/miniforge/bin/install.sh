#!/usr/bin/env bash

INSTALL_TEMPDIR=$(mktemp -d -t miniforge-XXXXXXXXXX)
url="https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
installer="${INSTALL_TEMPDIR}/Miniforge3.sh"

curl -fSL0o "${install_script}" "${url}" \
&& bash ${installer}

# https://github.com/conda-forge/miniforge
# bash <(curl -s Miniforge3.sh https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh)
# /usr/bin/bash < (curl -fsSL https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh)
# curl -fsSL0 https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh | sudo bash
# bash -x <( curl -fsSL0 https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh )
# curl -s https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh | sudo bash

# https://stackoverflow.com/questions/60935914/install-pypy-globally-ubuntu
# As @keith-thompson says, you can do sudo apt install pypy pypy-dev. If you want a more up-to-date version you can do snap install pypy pypy-dev. Another way to get a w
