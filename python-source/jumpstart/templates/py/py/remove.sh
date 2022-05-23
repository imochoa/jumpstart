#!/usr/bin/env bash

VENVDIR=${HOME}/.virtualenvs/trash-cli
INSTALLDIR=${HOME}/.local/bin

rm -r "${VENVDIR}"                       \
&& find "${INSTALLDIR}" -xtype l -delete
