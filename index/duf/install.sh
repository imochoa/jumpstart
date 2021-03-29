#!/usr/bin/env bash

sudo apt install -y wget git

VER=$(git ls-remote --refs --tags https://github.com/muesli/duf \
    | cut --delimiter='/' --fields=3     \
    | tr '-' '~'                         \
    | sort --version-sort                \
    | tail --lines=1);
# e.g. VER=v0.3.1

TMP_DEB=/tmp/duf.deb
wget https://github.com/muesli/duf/releases/download/${VER}/duf_${VER:1}_linux_amd64.deb --continue --output-document=${TMP_DEB}
sudo apt install ${TMP_DEB}
