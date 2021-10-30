#!/usr/bin/env bash


# INSTALL NEOVIM
VER=$(git ls-remote --refs --tags https://github.com/neovim/neovim |
  cut --delimiter='/' --fields=3 |
  tr '-' '~' |
  sort --version-sort |
  tail --lines=1)
# e.g. VER=v0.4.4

URL=https://github.com/neovim/neovim/releases/download/${VER}/nvim.appimage

# nvr expects "nvim" NOT "neovim"!
sudo rm -f /usr/local/bin/nvim \
  && sudo wget ${URL} --output-document=/usr/local/bin/nvim \
  && sudo chown ${USER}:${USER} /usr/local/bin/nvim \
  && sudo chmod +x /usr/local/bin/nvim \
  && sudo update-alternatives --install /usr/bin/nvim editor /usr/local/bin/nvim 100

# This last step might be more of a "setup" thing
