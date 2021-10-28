#!/usr/bin/env bash

sudo apt install -y wget git


VER=$(git ls-remote --refs --tags https://github.com/junegunn/fzf.git \
    | cut --delimiter='/' --fields=3     \
    | tr '-' '~'                         \
    | sort --version-sort                \
    | tail --lines=1);

URL="https://github.com/junegunn/fzf/releases/download/${VER}/fzf-${VER}-linux_amd64.tar.gz"
FZF_DIR=$(mktemp -d -t fzf-XXXXXXXXXX)

INSTALLPATH="/usr/bin/fzf"

wget ${URL}                                          \
  --continue                                         \
  --output-document="${FZF_DIR}/fzf.tar.gz"          \
&& tar -xzvf "${FZF_DIR}/fzf.tar.gz" -C "${FZF_DIR}" \
&& sudo rm -f "${INSTALLPATH}"                       \
&& sudo mv "${FZF_DIR}/fzf" "${INSTALLPATH}"         \
&& sudo chmod 0755 "${INSTALLPATH}"

 # overriding mode 0755 (rwxr-xr-x)?
