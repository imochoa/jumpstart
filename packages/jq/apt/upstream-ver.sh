#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: upstream-ver.sh
#		 >     Name: jq
#		 > Template: apt

printf "jq > %s\n" "$(apt-cache policy jq | grep Candidate | cut -d: -f2 | tr -d /" /")"
