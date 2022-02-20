#!/usr/bin/env sh

INSTALLDIR=/usr/local/bin
BASHCOMP=${BASHCOMP:-${HOME}/.config/bash/bash_completion}
ZSHCOMP=${ZSHCOMP:-${HOME}/.config/zsh/completions}


sudo apt-get install -y curl wget jq

URL=$(curl --silent "https://api.github.com/repos/sharkdp/fd/releases/latest" \
  | jq '..|.browser_download_url?' | grep 'x86_64' | grep 'linux' | grep 'gnu' \
  | tr -d '"' )


TEMPDIR=$(mktemp -d -t fdfind-XXXXXXXXXX)

echo "Downloading..."                                                               \
&& wget ${URL}                                                                      \
  --continue                                                                        \
  --output-document="${TEMPDIR}/data.tar.gz"                                        \
&& echo "extracting..."                                                             \
&& tar -xzvf "${TEMPDIR}/data.tar.gz" --directory="${TEMPDIR}"  --strip-components=1 \
&& echo "Installing..."                                                             \
&& sudo chmod +x "${TEMPDIR}/fd"                                                   \
&& sudo cp "${TEMPDIR}/fd" "${INSTALLDIR}/fdfind"                                         \
&& echo "Copying autocomplete files..."                                             \
&& sudo mkdir -p "${BASHCOMP}" \
&& sudo mkdir -p "${ZSHCOMP}" \
&& sudo cp "${TEMPDIR}/autocomplete/"*.bash* "${BASHCOMP}"                           \
&& sudo cp "${TEMPDIR}/autocomplete/_"* "${ZSHCOMP}"


## AUTOCOMPLETION SCRIPTS!
#AUTOURL=https://raw.githubusercontent.com/junegunn/fzf/master/shell/
#wget --output-document="${BASHCOMP}/fzf.bash" "${AUTOURL}/completion.bash"
#wget --output-document="${BASHCOMP}/fzf-key-bindings.bash" "${AUTOURL}/key-bindings.bash"
#
#wget --output-document="${ZSHCOMP}/_fzf.zsh" "${AUTOURL}/completion.zsh"
#wget --output-document="${ZSHCOMP}/_fzf-key-bindings.bash" "${AUTOURL}/key-bindings.zsh"
