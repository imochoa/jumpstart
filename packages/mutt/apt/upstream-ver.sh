#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: upstream-ver.sh
#		 >     Name: mutt
#		 > Template: apt

printf "mutt > %s\n" "$(apt-cache policy mutt | grep Candidate | cut -d: -f2 | tr -d /" /")"
