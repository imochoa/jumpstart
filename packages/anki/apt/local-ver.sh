#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: local-ver.sh
#		 >     Name: anki
#		 > Template: apt

printf "anki > %s\n" "$(apt-cache policy anki | grep Installed | cut -d: -f2 | tr -d /" /")"
