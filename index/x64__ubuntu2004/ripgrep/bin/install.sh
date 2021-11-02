#!/usr/bin/env sh

INSTALLDIR=/usr/local/bin
BASHCOMP=${BASHCOMP:-${HOME}/.config/bash/bash_completion}
ZSHCOMP=${ZSHCOMP:-${HOME}/.config/zsh/completions}

sudo apt-get install -y curl wget jq

URL=$(curl --silent "https://api.github.com/repos/BurntSushi/ripgrep/releases/latest" \
  | jq '..|.browser_download_url?' | grep 'x86_64' | grep 'linux' \
  | tr -d '"' )

TEMPDIR=$(mktemp -d -t ripgrep-XXXXXXXXXX)

echo "Downloading..."                                                               \
&& wget ${URL}                                                                      \
  --continue                                                                        \
  --output-document="${TEMPDIR}/data.tar.gz"                                        \
&& echo "extracting..."                                                             \
&& tar -xzvf "${TEMPDIR}/data.tar.gz" --directory="${TEMPDIR}" --strip-components=1 \
&& echo "Installing..."                                                             \
&& sudo chmod +x "${TEMPDIR}/rg"                                                   \
&& sudo cp "${TEMPDIR}/rg" "${INSTALLDIR}"                                         \
&& echo "Copying autocomplete files..."                                             \
&& sudo mkdir -p "${BASHCOMP}" \
&& sudo mkdir -p "${ZSHCOMP}" \
&& sudo cp "${TEMPDIR}/complete/"*.bash "${BASHCOMP}"                           \
&& sudo cp "${TEMPDIR}/complete/_"* "${ZSHCOMP}"
