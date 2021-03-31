#!/usr/bin/env bash

#DIR="${BASH_SOURCE%/*}"
#if [[ ! -d "$DIR" ]]; then DIR="$PWD"; fi
#. "$DIR/incl.sh"
#. "$DIR/main.sh"

VER=$(
  git ls-remote --refs --tags https://github.com/xxh/xxh |
    cut --delimiter='/' --fields=3 |
    tr '-' '~' |
    sort --version-sort |
    tail --lines=1
)
installdir=${HOME}/.local/bin
installpath=${installdir}/xxh

rm -rf "${installpath}" \
&& mkdir -p "${installdir}" \
&& wget https://github.com/xxh/xxh/releases/download/${VER}/xxh-x86_64.AppImage -O "${installpath}" \
&& chmod +x "${installpath}"
