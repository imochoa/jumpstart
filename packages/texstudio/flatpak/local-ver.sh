#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: local-ver.sh
#		 >     Name: TeX Studio
#		 > Template: flatpak

printf "org.texstudio.TeXstudio > %s\n" "$(flatpak info org.texstudio.TeXstudio | grep Version | cut -d: -f2 | tr -d /" /")"
