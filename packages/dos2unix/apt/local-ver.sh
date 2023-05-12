#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: local-ver.sh
#		 >     Name: dos2unix
#		 > Template: apt

printf "dos2unix > %s\n" "$(apt-cache policy dos2unix | grep Installed | cut -d: -f2 | tr -d /" /")"
