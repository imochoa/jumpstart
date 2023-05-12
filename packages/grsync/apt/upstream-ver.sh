#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: upstream-ver.sh
#		 >     Name: grsync
#		 > Template: apt

printf "grsync > %s\n" "$(apt-cache policy grsync | grep Candidate | cut -d: -f2 | tr -d /" /")"
