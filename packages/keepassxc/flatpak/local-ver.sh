#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: local-ver.sh
#		 >     Name: KeePassXC
#		 > Template: flatpak

printf "org.keepassxc.KeePassXC > %s\n" "$(flatpak info org.keepassxc.KeePassXC | grep Version | cut -d: -f2 | tr -d /" /")"
