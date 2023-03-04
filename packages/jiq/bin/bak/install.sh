#!/usr/bin/env sh

# TODO
https://github.com/fiatjaf/jiq/releases/download/v0.7.2/jiq_linux_amd64

# VER=$(curl --silent "https://api.github.com/repos/sharkdp/bat/releases/latest" | jq ".tag_name")

INSTALLDIR=/usr/local/bin
BASHCOMP=${BASHCOMP:-${HOME}/.config/bash/bash_completion}
ZSHCOMP=${ZSHCOMP:-${HOME}/.config/zsh/completions}

sudo apt-get install -y curl wget jq

URL=$(curl --silent "https://api.github.com/repos/fiatjaf/jiq/releases/latest" \
  | jq '..|.browser_download_url?' | grep 'x86_64' | grep 'linux' | grep 'gnu' \
  | tr -d '"' )

TEMPDIR=$(mktemp -d -t bat-XXXXXXXXXX)

echo "Downloading..."                                                               \
&& wget ${URL}                                                                      \
  --continue                                                                        \
  --output-document="${TEMPDIR}/data.tar.gz"                                        \
&& echo "extracting..."                                                             \
&& tar -xzvf "${TEMPDIR}/data.tar.gz" --directory="${TEMPDIR}" --strip-components=1 \
&& echo "Installing..."                                                             \
&& sudo chmod +x "${TEMPDIR}/bat"                                                   \
&& sudo cp "${TEMPDIR}/bat" "${INSTALLDIR}"                                         \
&& echo "Copying autocomplete files..."                                             \
&& sudo mkdir -p "${BASHCOMP}" \
&& sudo mkdir -p "${ZSHCOMP}" \
&& sudo cp "${TEMPDIR}/autocomplete/"*.bash "${BASHCOMP}"                           \
&& sudo cp "${TEMPDIR}/autocomplete/"*.zsh "${ZSHCOMP}"
