#!/usr/bin/env bash

INSTALLDIR=/usr/local/bin
BASHCOMP=${BASHCOMP:-${HOME}/.config/bash/bash_completion}
ZSHCOMP=${ZSHCOMP:-${HOME}/.config/zsh/completions}


sudo apt-get install -y curl wget jq

URL=$(curl --silent "https://api.github.com/repos/junegunn/fzf/releases/latest" \
  | jq '..|.browser_download_url?' | grep 'amd64' | grep 'linux' \
  | tr -d '"' )

AUTOURL=https://raw.githubusercontent.com/junegunn/fzf/master/shell/

TEMPDIR=$(mktemp -d -t fzf-XXXXXXXXXX)

echo "Downloading..."                                                               \
&& wget ${URL}                                                                      \
  --continue                                                                        \
  --output-document="${TEMPDIR}/data.tar.gz"                                        \
&& echo "extracting..."                                                             \
&& tar -xzvf "${TEMPDIR}/data.tar.gz" --directory="${TEMPDIR}"  \
&& echo "Installing..."                                                             \
&& sudo chmod +x "${TEMPDIR}/fzf"                                                   \
&& sudo cp "${TEMPDIR}/fzf" "${INSTALLDIR}"                                         \
&& echo "Copying autocomplete files..."                                             \
&& sudo mkdir -p "${BASHCOMP}" \
&& sudo mkdir -p "${ZSHCOMP}" \
&& sudo cp "${TEMPDIR}/complete/"*.bash "${BASHCOMP}"                           \
&& sudo cp "${TEMPDIR}/complete/_"* "${ZSHCOMP}"


# AUTOCOMPLETION SCRIPTS!
wget --output-document="${BASHCOMP}/fzf.bash" "${AUTOURL}/completion.bash"
wget --output-document="${BASHCOMP}/fzf-key-bindings.bash" "${AUTOURL}/key-bindings.bash"

wget --output-document="${ZSHCOMP}/_fzf.zsh" "${AUTOURL}/completion.zsh"
wget --output-document="${ZSHCOMP}/_fzf-key-bindings.bash" "${AUTOURL}/key-bindings.zsh"
