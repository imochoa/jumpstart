#!/usr/bin/env bash

VENVDIR=${HOME}/.virtualenvs/trash-cli
INSTALLDIR=${HOME}/.local/bin

mkdir -p "${VENVDIR}"                                            \
  && python -m venv "${VENVDIR}"                                 \
  && "${VENVDIR}/bin/pip" install --upgrade pip setuptools wheel \
  && "${VENVDIR}/bin/pip" install --upgrade trash-cli \
  && ln -s ${VENVDIR}/bin/trash** "${INSTALLDIR}"
