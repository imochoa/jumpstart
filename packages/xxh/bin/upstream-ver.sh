#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: upstream-ver.sh
#		 >     Name: xxh
#		 > Template: bin

# Commands
VER=$(curl -Ls -o /dev/null -w %{url_effective} https://github.com/xxh/xxh/releases/latest | rev | cut -d/ -f1 | rev) \
&& printf "\e[0;34m%-6s\e[m\n" "xxh > ${VER}\n"
