#!/usr/bin/env bash

# Snap can't read config files at ~/.config/cheat 
# sudo snap install --classic cheat

VER=$(git ls-remote --refs --tags https://github.com/cheat/cheat |
      cut --delimiter='/' --fields=3 |
      tail --lines=1)
url="https://github.com/cheat/cheat/releases/download/${VER}/cheat-linux-amd64.gz"

installdir="${HOME}/.local/bin"
# installdir="/usr/local/bin"

TEMPDIR=$(mktemp -d -t cheat-XXXXXXXXXX)

wget ${url}                                                \
  --continue                                               \
  --output-document="${TEMPDIR}/cheat-linux-amd64.gz"      \
&& gzip -d "${TEMPDIR}/cheat-linux-amd64.gz"               \
&& mv "${TEMPDIR}/cheat-linux-amd64" "${installdir}/cheat" \
&& chmod +x "${installdir}/cheat"


echo "LOOK UP THE SHELL AUTOCOMPLETION HELPERS FOR CHEAT!";
