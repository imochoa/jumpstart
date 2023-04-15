#!/usr/bin/env sh
# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 > INSTALL.SH
#		 > delta
#		 > bin

# Variables
INSTALL_DST="${INSTALL_DST:-${HOME}/.local/bin/}"
BASHCOMP_P="${BASHCOMP_P:-${HOME}/.config/bash/bash_completion}"
ZSHCOMP="${ZSHCOMP:-${HOME}/.config/zsh/completions}"
TEMPDIR="$(mktemp -d -t XXXXXXXXXX)"
FMT='\e[0;34m%-6s\e[m\n'
# Commands
DLTMP=$(mktemp -d -t jumpstart-XXXXXXXXXX) \
    && cd "${DLTMP}" \
    && printf "\e[0;34m%-6s\e[m\n" "Downloading to $(realpath .)" \
    && URL=$(curl --silent 'https://api.github.com/repos/dandavison/delta/releases/latest' | jq '..|.browser_download_url? | select( . != null )' | tr -d '"' | grep --ignore-case 'linux' | grep --ignore-case 'x86_64' | grep --ignore-case 'gnu') \
    && curl -jLO "${URL}" \
    && DLFILE=$(ls . | head -n1) \
    && printf "\e[0;34m%-6s\e[m\n" "Extracting..." \
    && tar -xzvf "${DLFILE}" \
    && rm "${DLFILE}" \
    && echo "$(ls .)" \
    && SRCPATH=$( find . -type f | grep --ignore-case 'delta' ) \
    && sudo chmod +x "${SRCPATH}" \
    && sudo mv "${SRCPATH}" "${INSTALL_DST}/delta"