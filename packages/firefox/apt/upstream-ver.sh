#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: upstream-ver.sh
#		 >     Name: Firefox
#		 > Template: apt

printf "firefox > %s\n" "$(apt-cache policy firefox | grep Candidate | cut -d: -f2 | tr -d /" /")"
