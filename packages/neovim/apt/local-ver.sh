#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: local-ver.sh
#		 >     Name: neovim
#		 > Template: apt

printf "neovim > %s\n" "$(apt-cache policy neovim | grep Installed | cut -d: -f2 | tr -d /" /")"
printf "python3-neovim > %s\n" "$(apt-cache policy python3-neovim | grep Installed | cut -d: -f2 | tr -d /" /")"
