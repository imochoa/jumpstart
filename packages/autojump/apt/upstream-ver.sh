#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: upstream-ver.sh
#		 >     Name: autojump
#		 > Template: apt

printf "autojump > %s\n" "$(apt-cache policy autojump | grep Candidate | cut -d: -f2 | tr -d /" /")"
