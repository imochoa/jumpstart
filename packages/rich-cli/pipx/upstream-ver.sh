#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: upstream-ver.sh
#		 >     Name: rich-cli
#		 > Template: pipx

VER=$(curl --silent -JL "https://pypi.org/project/rich-cli/" | grep --ignore-case --after-context=2 "release__version\"" | grep -v --ignore-case "class" | head -n1 | tr -s " ") \
&& printf "\e[0;34m%-6s\e[m\n" "[rich-cli] version was: ${VER}"
