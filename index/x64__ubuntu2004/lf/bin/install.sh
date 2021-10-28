#!/usr/bin/env bash

#DIR="${BASH_SOURCE%/*}"
#if [[ ! -d "$DIR" ]]; then DIR="$PWD"; fi
#. "$DIR/incl.sh"
#. "$DIR/main.sh"

VER=$(
  git ls-remote --refs --tags https://github.com/gokcehan/lf |
    cut --delimiter='/' --fields=3 |
    tr '-' '~' |
    sort --version-sort |
    tail --lines=1
)
installdir=${HOME}/.local/bin
installpath=${installdir}/lf

INSTALL_TEMPDIR=$(mktemp -d -t lf-XXXXXXXXXX)

rm -rf ${installpath} \
&& wget "https://github.com/gokcehan/lf/releases/download/${VER}/lf-linux-amd64.tar.gz" \
  --output-document "${INSTALL_TEMPDIR}/lf.tar.gz" \
&& tar xvf "${INSTALL_TEMPDIR}/lf.tar.gz" --directory="${INSTALL_TEMPDIR}" \
&& chmod +x "${INSTALL_TEMPDIR}/lf" \
&& mv "${INSTALL_TEMPDIR}/lf" "${installpath}"
