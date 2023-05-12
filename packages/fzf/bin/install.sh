#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: install.sh
#		 >     Name: fzf
#		 > Template: bin

# Variables

# Commands
DLTMP=$(mktemp -d -t jumpstart-XXXXXXXXXX) \
&& cd "${DLTMP}" \
&& printf "\e[0;34m%-6s\e[m\n" "Downloading to $(realpath .)" \
&& URL=$(curl --silent 'https://api.github.com/repos/junegunn/fzf/releases/latest' | jq '..|.browser_download_url? | select( . != null )' | tr -d '"' | grep --ignore-case 'linux' | grep --ignore-case 'amd64') \
&& curl -jLO "${URL}" \
&& DLFILE=$(ls . | head -n1) \
&& printf "\e[0;34m%-6s\e[m\n" "Extracting..." \
&& tar -xzvf "${DLFILE}" \
&& rm "${DLFILE}" \
&& echo "$(ls .)" \
&& SRCPATH=$( find . -type f | grep --ignore-case 'fzf' ) \
&& sudo chmod +x "${SRCPATH}" \
&& sudo mv "${SRCPATH}" "${INSTALL_DST}/fzf"

# <<<POST STAGE>>>

# TODO download and put into correct location
echo "https://github.com/junegunn/fzf/tree/master/shell"
