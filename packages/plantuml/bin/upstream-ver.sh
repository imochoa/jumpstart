#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: upstream-ver.sh
#		 >     Name: plantuml
#		 > Template: bin

# Commands
VER=$(curl -Ls -o /dev/null -w %{url_effective} https://github.com/plantuml/plantuml/releases/latest | rev | cut -d/ -f1 | rev) \
&& printf "\e[0;34m%-6s\e[m\n" "plantuml > ${VER}\n"
