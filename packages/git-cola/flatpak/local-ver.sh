#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: local-ver.sh
#		 >     Name: Git Cola
#		 > Template: flatpak

printf "com.github.git_cola.git-cola > %s\n" "$(flatpak info com.github.git_cola.git-cola | grep Version | cut -d: -f2 | tr -d /" /")"
