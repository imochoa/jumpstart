#!/usr/bin/env sh
# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 > INSTALL.SH
#		 > nvm
#		 > bin

# Variables
INSTALL_DST="${INSTALL_DST:-${{HOME}}/.local/bin/}"
BASHCOMP_P="${BASHCOMP_P:-${HOME}/.config/bash/bash_completion}"
ZSHCOMP="${ZSHCOMP:-${HOME}/.config/zsh/completions}"
TEMPDIR="$(mktemp -d -t XXXXXXXXXX)"
FMT='\e[0;34m%-6s\e[m\n'
# Commands
DLTMP=$(mktemp -d -t jumpstart-XXXXXXXXXX) \
    && cd "${DLTMP}" \
    && printf "\e[0;34m%-6s\e[m\n" "Downloading to $(realpath .)" \
    && URL=$() \
    && curl -jLO "${URL}" \
    && DLFILE=$(ls . | head -n1)

# <<<POST STAGE>>>

#


# https://github.com/nvm-sh/nvm
# ToDo get latest? and not 0.39.3
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash

# Deeper shell integration
# https://github.com/nvm-sh/nvm#deeper-shell-integration

# Update ?
nvm install-latest-npm

# Install node ?
nvm install --lts
