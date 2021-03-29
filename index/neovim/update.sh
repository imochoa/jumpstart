#!/usr/bin/env bash

VER=$(git ls-remote --refs --tags https://github.com/neovim/neovim |
  cut --delimiter='/' --fields=3 |
  tr '-' '~' |
  sort --version-sort |
  tail --lines=1)
# e.g. VER=v0.4.4

sudo rm -f /usr/local/bin/nvim \
&& sudo wget https://github.com/neovim/neovim/releases/download/${VER}/nvim.appimage --output-document=/usr/local/bin/nvim \
&& sudo chown ${USER}:${USER} /usr/local/bin/nvim \
&& sudo chmod +x /usr/local/bin/nvim
