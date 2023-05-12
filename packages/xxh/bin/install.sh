#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: install.sh
#		 >     Name: xxh
#		 > Template: bin

# Variables

# Commands
DLTMP=$(mktemp -d -t jumpstart-XXXXXXXXXX) \
&& cd "${DLTMP}" \
&& printf "\e[0;34m%-6s\e[m\n" "Downloading to $(realpath .)" \
&& URL=$(curl --silent 'https://api.github.com/repos/xxh/xxh/releases/latest' | jq '..|.browser_download_url? | select( . != null )' | tr -d '"' | grep --ignore-case 'linux' | grep --ignore-case 'portable' | grep --ignore-case 'x86_64') \
&& curl -jLO "${URL}" \
&& DLFILE=$(ls . | head -n1) \
&& printf "\e[0;34m%-6s\e[m\n" "Extracting..." \
&& tar -xzvf "${DLFILE}" \
&& rm "${DLFILE}" \
&& echo "$(ls .)" \
&& SRCPATH=$( find . -type f | grep --ignore-case 'xxh' ) \
&& sudo chmod +x "${SRCPATH}" \
&& sudo mv "${SRCPATH}" "${INSTALL_DST}/xxh"

# <<<POST STAGE>>>

