#!/usr/bin/env bash

INSTALLDIR=/usr/local/bin
BINPATH=${INSTALLDIR}/cheat

[ -f "${BINPATH}" ] && sudo rm "${BINPATH}" || echo "Not installed"
