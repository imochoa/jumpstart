#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: upstream-ver.sh
#		 >     Name: httrack
#		 > Template: apt

printf "webhttrack > %s\n" "$(apt-cache policy webhttrack | grep Candidate | cut -d: -f2 | tr -d /" /")"
