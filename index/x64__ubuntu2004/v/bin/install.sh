#!/usr/bin/env bash

URL='https://raw.githubusercontent.com/rupa/v/master/v'

sudo apt install -y curl

USERINSTALL="${HOME}/.local/bin"
SYSINSTALL="/usr/local/bin"

echo $USERINSTALL
curl $URL --output "${USERINSTALL}/v" && sudo chmod +x "${USERINSTALL}/v"
