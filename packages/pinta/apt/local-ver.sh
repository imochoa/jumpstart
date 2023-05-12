#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: local-ver.sh
#		 >     Name: pinta
#		 > Template: apt

printf "pinta > %s\n" "$(apt-cache policy pinta | grep Installed | cut -d: -f2 | tr -d /" /")"
