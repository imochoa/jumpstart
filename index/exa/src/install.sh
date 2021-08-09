#!/usr/bin/env bash
# After Ubuntu 20.10
#sudo apt install -y exa
# Before...
VER=$(git ls-remote --refs --tags https://github.com/ogham/exa \
    | cut --delimiter='/' --fields=3     \
    | tr '-' '~'                         \
    | sort --version-sort                \
    | tail --lines=1                     \
    | tr -d 'v'
    );
# e.g. VER=v1.2.0
rm -rf /tmp/exa \
&& mkdir -p /tmp/exa/ \
&& mkdir -p ~/.local/bin \
&& wget https://github.com/ogham/exa/releases/download/v${VER}/exa-linux-x86_64-${VER}.zip -O /tmp/exa/exa.zip \
&& unzip /tmp/exa/exa.zip -d /tmp/exa \
&& rm /tmp/exa/exa.zip \
&& mv /tmp/exa/*  ~/.local/bin/exa \
&& chmod +x ~/.local/bin/exa
