#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: upstream-ver.sh
#		 >     Name: pipe-viewer
#		 > Template: apt

printf "pv > %s\n" "$(apt-cache policy pv | grep Candidate | cut -d: -f2 | tr -d /" /")"
