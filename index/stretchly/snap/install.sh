#!/usr/bin/env bash

sudo snap install stretchly

# VER=$(git ls-remote --refs --tags https://github.com/hovancik/stretchly \
#     | cut --delimiter='/' --fields=3     \
#     | tr '-' '~'                         \
#     | sort --version-sort                \
#     | tail --lines=1);
# # e.g. VER=v1.2.0
# sudo rm -f /usr/local/bin/stretchly \
# && sudo wget https://github.com/hovancik/stretchly/releases/download/${VER}/Stretchly-${VER:1}.AppImage \
#     --output-document=/usr/local/bin/stretchly \
# && sudo chmod +x /usr/local/bin/stretchly;
