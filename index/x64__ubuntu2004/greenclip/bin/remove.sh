#!/usr/bin/env bash

INSTALL_PATH="${HOME}/.local/bin/greenclip";

if test -f "$INSTALL_PATH"; then
    rm ${INSTALL_PATH}
fi
