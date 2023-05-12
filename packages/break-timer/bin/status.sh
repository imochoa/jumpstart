#!/usr/bin/env sh

# TODO
INSTALLDIR=/usr/local/bin
BINPATH=${INSTALLDIR}/bat

[ -f "${BINPATH}" ] && echo "bat -> [installed!]" || echo "bat -> Not installed"
