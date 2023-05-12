#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: upstream-ver.sh
#		 >     Name: meld
#		 > Template: apt

printf "meld > %s\n" "$(apt-cache policy meld | grep Candidate | cut -d: -f2 | tr -d /" /")"
