#!/usr/bin/env sh

# VER=$(curl --silent "https://api.github.com/repos/sharkdp/bat/releases/latest" | jq ".tag_name")

INSTALLDIR=/usr/local/bin
BASHCOMP=${BASHCOMP:-${HOME}/.config/bash/bash_completion}
ZSHCOMP=${ZSHCOMP:-${HOME}/.config/zsh/completions}

sudo apt-get install -y curl wget jq

VER=$(git ls-remote --refs --tags https://github.com/cheat/cheat |
      cut --delimiter='/' --fields=3 |
      tail --lines=1)

URL="https://github.com/cheat/cheat/releases/download/${VER}/cheat-linux-amd64.gz"

TEMPDIR=$(mktemp -d -t cheat-XXXXXXXXXX)

echo "Downloading..."                                                                                 \
&& wget ${URL}                                                                                        \
  --continue                                                                                          \
  --output-document="${TEMPDIR}/cheat.gz"                                                             \
&& echo "extracting..."                                                                               \
&& gzip -d "${TEMPDIR}/cheat.gz"                                                                      \
&& echo "Installing..."                                                                               \
&& sudo chmod +x "${TEMPDIR}/cheat"                                                                   \
&& sudo cp "${TEMPDIR}/cheat" "${INSTALLDIR}"                                                         \
&& echo "Copying autocomplete files..."                                                               \
&& sudo wget -P "${BASHCOMP}" https://raw.githubusercontent.com/cheat/cheat/master/scripts/cheat.bash \
&& sudo wget -P "${ZSHCOMP}" https://raw.githubusercontent.com/cheat/cheat/master/scripts/cheat.zsh
&& echo "installing the cheatsheets command" \
&& sudo wget -O "${INSTALLDIR}/cheatsheets" https://raw.githubusercontent.com/cheat/cheat/master/scripts/git/cheatsheets \
&& sudo chmod +x "${INSTALLDIR}/cheatsheets" \
&& mkdir -p ~/.config/cheat/cheatsheets/community \
&& mkdir -p ~/.config/cheat/cheatsheets/personal
