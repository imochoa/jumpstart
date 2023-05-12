#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: upstream-ver.sh
#		 >     Name: dunst
#		 > Template: apt

printf "dunst > %s\n" "$(apt-cache policy dunst | grep Candidate | cut -d: -f2 | tr -d /" /")"
