#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: upstream-ver.sh
#		 >     Name: Git Cola
#		 > Template: apt

printf "git-cola > %s\n" "$(apt-cache policy git-cola | grep Candidate | cut -d: -f2 | tr -d /" /")"
