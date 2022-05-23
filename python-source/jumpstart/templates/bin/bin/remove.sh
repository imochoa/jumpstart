#!/usr/bin/env sh

INSTALLDIR=/usr/local/bin
BINPATH=${INSTALLDIR}/bat

[ -f "${BINPATH}" ] && sudo rm "${BINPATH}" || echo "Not installed"
