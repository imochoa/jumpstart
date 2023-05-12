#!/usr/bin/env sh
# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: install.sh
#		 >     Name: shellcheck
#		 > Template: bin

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
&& URL=$(curl --silent 'https://api.github.com/repos/koalaman/shellcheck/releases/latest' | jq '..|.browser_download_url? | select( . != null )' | tr -d '"' | grep --ignore-case 'linux' | grep --ignore-case 'x86_64') \
&& curl -jLO "${URL}" \
&& DLFILE=$(ls . | head -n1) \
&& printf "\e[0;34m%-6s\e[m\n" "Extracting..." \
&& tar -xf "${DLFILE}" \
&& rm "${DLFILE}" \
&& echo "$(ls .)" \
&& SRCPATH=$( find . -type f | grep --ignore-case 'shellcheck$' ) \
&& sudo chmod +x "${SRCPATH}" \
&& sudo mv "${SRCPATH}" "${INSTALL_DST}/shellcheck"
