#!/usr/bin/env bash

https://github.com/aristocratos/btop/releases/download/v1.0.20/btop-1.0.20-x86_64-linux-musl.tbz

./install.sh

VER=$(git ls-remote --refs --tags https://github.com/aristocratos/btop |
  cut --delimiter='/' --fields=3 |
  tr '-' '~v' |
  sort --version-sort |
  tail --lines=1 |
  tr -d 'v'
)
# e.g. VER=v0.4.4
echo $VER
# https://github.com/aristocratos/btop/releases/download/v1.0.11/btop-1.0.11-linux-x86_64.tbz
URL=https://github.com/aristocratos/btop/releases/download/v${VER}/btop-${VER}-linux-x86_64.tbz

BPTOP_DIR=$(mktemp -d -t btop-XXXXXXXXXX)
BPTOP_TBZ="${BPTOP_DIR}/btop.tbz"

echo $URL
echo "Installing btop++" \
&& sudo chown $USER:$USER ${BPTOP_DIR} \
&& wget ${URL} --output-document=${BPTOP_TBZ} \
&& cd ${BPTOP_DIR} \
&& tar -xvjf ${BPTOP_TBZ} \
&& sudo make install \
&& sudo make setuid
