#!/usr/bin/env bash

INSTALLDIR=/usr/local/bin
BINPATH=${INSTALLDIR}/cheat

[ -f "${BINPATH}" ] && echo "cheat [Installed]" || echo "cheat [Not installed]"
