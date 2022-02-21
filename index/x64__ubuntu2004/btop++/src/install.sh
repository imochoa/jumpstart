#!/usr/bin/env bash

sudo apt-get install -y curl jq

URL=$(curl --silent "https://api.github.com/repos/aristocratos/btop/releases/latest" \
    | jq '..|.browser_download_url?' | grep 'x86_64' | grep 'linux' \
    | tr -d '"' )

BPTOP_DIR=$(mktemp -d -t btop-XXXXXXXXXX)
BPTOP_TBZ="${BPTOP_DIR}/btop.tbz"

echo "Installing btop++" \
&& sudo chown $USER:$USER ${BPTOP_DIR} \
&& wget ${URL} --output-document=${BPTOP_TBZ} \
&& cd ${BPTOP_DIR} \
&& tar -xvjf ${BPTOP_TBZ} \
&& sudo make install \
&& sudo make setuid

