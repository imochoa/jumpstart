#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: upstream-ver.sh
#		 >     Name: pavucontrol
#		 > Template: apt

printf "pavucontrol > %s\n" "$(apt-cache policy pavucontrol | grep Candidate | cut -d: -f2 | tr -d /" /")"
