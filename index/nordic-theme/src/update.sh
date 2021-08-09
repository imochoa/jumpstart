#!/usr/bin/env bash

[ -d "${HOME}/.themes/Nordic/.git" ] && (cd "${HOME}/.themes/Nordic" && git pull)
[ -d "/usr/share/themes/Nordic/.git" ] && (cd /usr/share/themes/Nordic && git pull)
