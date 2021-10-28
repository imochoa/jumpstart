#!/usr/bin/env bash

# Snap can't read config files at ~/.config/cheat
# sudo snap remove cheat

installdir="${HOME}/.local/bin"
# installdir="/usr/local/bin"

rm -f "${installdir}/cheat"

echo "LOOK UP THE SHELL AUTOCOMPLETION HELPERS FOR CHEAT!";
