#!/usr/bin/env bash

VER=$(git ls-remote --refs --tags https://github.com/peazip/PeaZip \
    | cut --delimiter='/' --fields=3     \
    | tr '-' '~'                         \
    | sort --version-sort                \
    | tail --lines=1);
URL="https://github.com/peazip/PeaZip/releases/download/${VER}/peazip_${VER}.LINUX.x86_64.GTK2.deb"

# INSTALL_TEMPDIR=$(mktemp -d -t peazip-XXXXXXXXXX)
# TMP_DEB="${INSTALL_TEMPDIR}/peazip.deb"
TMP_DEB="/tmp/peazip.deb"

echo $VER
wget "${URL}" \
  --continue \
  --output-document=${TMP_DEB} \
&& sudo apt install ${TMP_DEB}

