#!/usr/bin/env sh

# VER=$(curl --silent "https://api.github.com/repos/sharkdp/bat/releases/latest" | jq ".tag_name")

INSTALLDIR=/usr/local/bin
BINPATH=${INSTALLDIR}/bat

[ -f "${BINPATH}" ] && sudo rm "${BINPATH}" || echo "Not installed"
